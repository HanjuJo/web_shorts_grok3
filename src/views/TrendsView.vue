&lt;template>
  &lt;div class="trends-view">
    &lt;h1>트렌드 분석&lt;/h1>
    
    &lt;div v-if="loading" class="loading">
      데이터를 불러오는 중...
    &lt;/div>

    &lt;div v-else-if="error" class="error">
      {{ error }}
    &lt;/div>

    &lt;div v-else-if="trendingVideos.length === 0" class="no-data">
      표시할 트렌드 데이터가 없습니다.
    &lt;/div>

    &lt;div v-else class="video-grid">
      &lt;div v-for="video in trendingVideos" :key="video.videoId" class="video-card">
        &lt;img :src="video.thumbnailUrl" :alt="video.title" class="thumbnail">
        &lt;div class="video-info">
          &lt;h3>{{ video.title }}&lt;/h3>
          &lt;div class="stats">
            &lt;span>&lt;i class="fas fa-eye">&lt;/i> {{ formatNumber(video.viewCount) }}&lt;/span>
            &lt;span>&lt;i class="fas fa-thumbs-up">&lt;/i> {{ formatNumber(video.likeCount) }}&lt;/span>
            &lt;span>&lt;i class="fas fa-comment">&lt;/i> {{ formatNumber(video.commentCount) }}&lt;/span>
          &lt;/div>
        &lt;/div>
      &lt;/div>
    &lt;/div>

    &lt;button @click="refreshTrends" class="refresh-btn" :disabled="loading">
      &lt;i class="fas fa-sync-alt">&lt;/i> 새로고침
    &lt;/button>
  &lt;/div>
&lt;/template>

&lt;script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'TrendsView',
  computed: {
    ...mapState(['trendingVideos', 'loading', 'error'])
  },
  methods: {
    ...mapActions(['fetchTrendingVideos']),
    formatNumber(num) {
      return new Intl.NumberFormat('ko-KR').format(num)
    },
    async refreshTrends() {
      await this.fetchTrendingVideos()
    }
  },
  created() {
    console.log('TrendsView created')
    this.fetchTrendingVideos()
  },
  mounted() {
    console.log('TrendsView mounted')
  }
}
&lt;/script>

&lt;style scoped>
.trends-view {
  padding: 20px;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.video-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.video-card:hover {
  transform: translateY(-2px);
}

.thumbnail {
  width: 100%;
  aspect-ratio: 16/9;
  object-fit: cover;
}

.video-info {
  padding: 15px;
}

.video-info h3 {
  margin: 0 0 10px 0;
  font-size: 16px;
  line-height: 1.4;
  height: 2.8em;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.stats {
  display: flex;
  gap: 15px;
  color: #666;
  font-size: 14px;
}

.stats i {
  margin-right: 5px;
}

.loading, .error, .no-data {
  text-align: center;
  padding: 40px;
  color: #666;
}

.error {
  color: #dc3545;
}

.refresh-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #1a73e8;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 25px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: all 0.2s;
}

.refresh-btn:hover:not(:disabled) {
  background: #1557b0;
  transform: translateY(-2px);
}

.refresh-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.refresh-btn i {
  font-size: 16px;
}
&lt;/style>
