from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import sqlite3
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()

# YouTube API setup
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def init_db():
    conn = sqlite3.connect('creator_tool.db')
    c = conn.cursor()
    
    # 채널 분석 결과를 저장하는 테이블
    c.execute('''CREATE TABLE IF NOT EXISTS channel_analytics 
                (id INTEGER PRIMARY KEY, 
                channel_id TEXT,
                subscriber_count INTEGER,
                view_count INTEGER,
                video_count INTEGER,
                analysis_date TIMESTAMP)''')
    
    # 트렌드 데이터를 저장하는 테이블
    c.execute('''CREATE TABLE IF NOT EXISTS trends
                (id INTEGER PRIMARY KEY,
                video_id TEXT,
                title TEXT,
                view_count INTEGER,
                like_count INTEGER,
                comment_count INTEGER,
                trending_date TIMESTAMP)''')
    
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def hello():
    return "Creator Tool API is running!"

@app.route('/api/features')
def get_features():
    features = [
        {
            "id": 1,
            "name": "YouTube 트렌드 분석",
            "description": "실시간 인기 동영상 트렌드 분석"
        },
        {
            "id": 2,
            "name": "채널 분석",
            "description": "상세한 채널 성과 분석 및 인사이트 제공"
        }
    ]
    return jsonify(features)

@app.route('/api/trends')
def get_trends():
    try:
        # YouTube Data API를 사용하여 인기 동영상 가져오기
        request = youtube.videos().list(
            part="snippet,statistics",
            chart="mostPopular",
            regionCode="KR",
            maxResults=10
        )
        response = request.execute()
        
        trends = []
        for item in response['items']:
            trend = {
                'videoId': item['id'],
                'title': item['snippet']['title'],
                'thumbnailUrl': item['snippet']['thumbnails']['high']['url'],
                'viewCount': item['statistics']['viewCount'],
                'likeCount': item.get('statistics', {}).get('likeCount', '0'),
                'commentCount': item.get('statistics', {}).get('commentCount', '0'),
                'publishedAt': item['snippet']['publishedAt']
            }
            trends.append(trend)
            
            # DB에 트렌드 데이터 저장
            conn = sqlite3.connect('creator_tool.db')
            c = conn.cursor()
            c.execute('''INSERT INTO trends 
                        (video_id, title, view_count, like_count, comment_count, trending_date)
                        VALUES (?, ?, ?, ?, ?, ?)''',
                        (item['id'],
                        item['snippet']['title'],
                        int(item['statistics']['viewCount']),
                        int(item.get('statistics', {}).get('likeCount', 0)),
                        int(item.get('statistics', {}).get('commentCount', 0)),
                        datetime.now()))
            conn.commit()
            conn.close()
        
        return jsonify({'success': True, 'trends': trends})
    except Exception as e:
        print('Error in get_trends:', str(e))
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/channel/analyze', methods=['POST'])
def analyze_channel():
    try:
        data = request.get_json()
        channel_id = data.get('channelId')
        
        if not channel_id:
            return jsonify({'success': False, 'error': 'Channel ID is required'}), 400
        
        # 채널 정보 가져오기
        channel_request = youtube.channels().list(
            part="snippet,statistics",
            id=channel_id
        )
        channel_response = channel_request.execute()
        
        if not channel_response['items']:
            return jsonify({'success': False, 'error': 'Channel not found'}), 404
        
        channel_data = channel_response['items'][0]
        
        # 최근 동영상 목록 가져오기
        videos_request = youtube.search().list(
            part="id,snippet",
            channelId=channel_id,
            order="date",
            type="video",
            maxResults=50
        )
        videos_response = videos_request.execute()
        
        # 분석 결과 생성
        analysis = {
            'channelTitle': channel_data['snippet']['title'],
            'subscriberCount': channel_data['statistics']['subscriberCount'],
            'viewCount': channel_data['statistics']['viewCount'],
            'videoCount': channel_data['statistics']['videoCount'],
            'recentVideos': [{
                'title': video['snippet']['title'],
                'publishedAt': video['snippet']['publishedAt'],
                'thumbnailUrl': video['snippet']['thumbnails']['high']['url']
            } for video in videos_response['items']],
            'analysisDate': datetime.now().isoformat()
        }
        
        # DB에 분석 결과 저장
        conn = sqlite3.connect('creator_tool.db')
        c = conn.cursor()
        c.execute('''INSERT INTO channel_analytics 
                    (channel_id, subscriber_count, view_count, video_count, analysis_date)
                    VALUES (?, ?, ?, ?, ?)''',
                    (channel_id, 
                    int(channel_data['statistics']['subscriberCount']),
                    int(channel_data['statistics']['viewCount']),
                    int(channel_data['statistics']['videoCount']),
                    datetime.now()))
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'analysis': analysis})
    except Exception as e:
        print('Error in analyze_channel:', str(e))
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/trends/history')
def get_trends_history():
    try:
        conn = sqlite3.connect('creator_tool.db')
        c = conn.cursor()
        c.execute('''
            SELECT video_id, title, view_count, trending_date
            FROM trends
            ORDER BY trending_date DESC
            LIMIT 100
        ''')
        rows = c.fetchall()
        conn.close()
        
        trends_history = [{
            'videoId': row[0],
            'title': row[1],
            'viewCount': row[2],
            'trendingDate': row[3]
        } for row in rows]
        
        return jsonify({'success': True, 'trendsHistory': trends_history})
    except Exception as e:
        print('Error in get_trends_history:', str(e))
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/analyze-video', methods=['POST'])
def analyze_video():
    try:
        data = request.json
        video_url = data.get('videoUrl')
        
        # YouTube 비디오 ID 추출
        if 'youtube.com/watch?v=' in video_url:
            video_id = video_url.split('watch?v=')[1].split('&')[0]
        elif 'youtu.be/' in video_url:
            video_id = video_url.split('youtu.be/')[1]
        else:
            return jsonify({'error': '잘못된 YouTube URL입니다'}), 400

        # 비디오 정보 가져오기
        video_response = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=video_id
        ).execute()

        if not video_response['items']:
            return jsonify({'error': '비디오를 찾을 수 없습니다'}), 404

        video_data = video_response['items'][0]
        
        # 응답 데이터 구성
        analysis_result = {
            'thumbnail': video_data['snippet']['thumbnails']['high']['url'],
            'title': video_data['snippet']['title'],
            'channelName': video_data['snippet']['channelTitle'],
            'metrics': {
                'views': video_data['statistics'].get('viewCount', '0'),
                'likes': video_data['statistics'].get('likeCount', '0'),
                'comments': video_data['statistics'].get('commentCount', '0'),
                'duration': video_data['contentDetails']['duration']
            },
            'contentQuality': 4.5,  # AI 분석 결과 (예시)
            'qualityAnalysis': '영상의 화질과 음질이 우수하며, 주제 전달이 명확합니다.',
            'engagement': {
                '시청 유지율': 75,
                '좋아요 비율': 85,
                '댓글 참여도': 65
            },
            'suggestions': [
                {
                    'icon': 'fas fa-clock',
                    'title': '영상 길이 최적화',
                    'description': '시청자의 집중도를 고려할 때, 영상 길이를 8-10분으로 조정하는 것이 좋습니다.'
                },
                {
                    'icon': 'fas fa-tags',
                    'title': 'SEO 개선',
                    'description': '제목과 태그에 주요 키워드를 더 효과적으로 활용하면 검색 노출을 높일 수 있습니다.'
                },
                {
                    'icon': 'fas fa-users',
                    'title': '시청자 참여 유도',
                    'description': '영상 중간에 질문을 던지거나 의견을 묻는 등 시청자 참여를 유도하는 요소를 추가해보세요.'
                }
            ]
        }

        return jsonify(analysis_result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5003))
    app.run(host='0.0.0.0', port=port, debug=True)