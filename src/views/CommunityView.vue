&lt;template>
  &lt;div class="community">
    &lt;div class="community-header">
      &lt;h1>크리에이터 커뮤니티&lt;/h1>
      &lt;p>다른 크리에이터들과 경험을 공유하고 함께 성장하세요&lt;/p>
    &lt;/div>

    &lt;div class="community-content">
      &lt;div class="sidebar">
        &lt;div class="user-profile" v-if="isLoggedIn">
          &lt;img :src="user.avatar" :alt="user.name">
          &lt;h3>{{ user.name }}&lt;/h3>
          &lt;p>{{ user.role }}&lt;/p>
        &lt;/div>
        &lt;div class="login-prompt" v-else>
          &lt;p>로그인하고 커뮤니티에 참여하세요&lt;/p>
          &lt;button class="btn-primary">
            &lt;i class="fas fa-sign-in-alt">&lt;/i> 로그인
          &lt;/button>
        &lt;/div>
        
        &lt;div class="categories">
          &lt;h3>카테고리&lt;/h3>
          &lt;ul>
            &lt;li 
              v-for="category in categories" 
              :key="category.id"
              :class="{ active: selectedCategory === category.id }"
              @click="selectCategory(category.id)"
            >
              &lt;i :class="category.icon">&lt;/i>
              &lt;span>{{ category.name }}&lt;/span>
              &lt;span class="count">{{ category.count }}&lt;/span>
            &lt;/li>
          &lt;/ul>
        &lt;/div>

        &lt;div class="trending-tags">
          &lt;h3>인기 태그&lt;/h3>
          &lt;div class="tags">
            &lt;span 
              v-for="tag in trendingTags" 
              :key="tag.name"
              class="tag"
            >
              #{{ tag.name }}
              &lt;small>{{ tag.count }}&lt;/small>
            &lt;/span>
          &lt;/div>
        &lt;/div>
      &lt;/div>

      &lt;div class="main-content">
        &lt;div class="content-header">
          &lt;div class="search-box">
            &lt;input 
              type="text" 
              v-model="searchQuery"
              placeholder="게시글 검색..."
            >
            &lt;i class="fas fa-search">&lt;/i>
          &lt;/div>
          &lt;button class="btn-primary new-post-btn" @click="showNewPostModal">
            &lt;i class="fas fa-pen">&lt;/i> 새 게시글
          &lt;/button>
        &lt;/div>

        &lt;div class="posts">
          &lt;div v-for="post in filteredPosts" :key="post.id" class="post-card">
            &lt;div class="post-header">
              &lt;div class="user-info">
                &lt;img :src="post.author.avatar" :alt="post.author.name">
                &lt;div>
                  &lt;h4>{{ post.author.name }}&lt;/h4>
                  &lt;span>{{ post.createdAt }}&lt;/span>
                &lt;/div>
              &lt;/div>
              &lt;div class="post-category">
                &lt;i :class="getCategoryIcon(post.category)">&lt;/i>
                {{ getCategoryName(post.category) }}
              &lt;/div>
            &lt;/div>

            &lt;div class="post-content">
              &lt;h3>{{ post.title }}&lt;/h3>
              &lt;p>{{ post.excerpt }}&lt;/p>
              &lt;div class="post-tags">
                &lt;span v-for="tag in post.tags" :key="tag" class="tag">
                  #{{ tag }}
                &lt;/span>
              &lt;/div>
            &lt;/div>

            &lt;div class="post-footer">
              &lt;div class="interactions">
                &lt;button :class="{ active: post.liked }" @click="toggleLike(post)">
                  &lt;i class="fas fa-heart">&lt;/i>
                  {{ post.likes }}
                &lt;/button>
                &lt;button>
                  &lt;i class="fas fa-comment">&lt;/i>
                  {{ post.comments }}
                &lt;/button>
                &lt;button>
                  &lt;i class="fas fa-share">&lt;/i>
                  공유
                &lt;/button>
              &lt;/div>
            &lt;/div>
          &lt;/div>
        &lt;/div>
      &lt;/div>
    &lt;/div>
  &lt;/div>
&lt;/template>

&lt;script>
export default {
  name: 'CommunityView',
  data() {
    return {
      isLoggedIn: true, // 임시 데이터
      user: {
        name: '김크리에이터',
        role: '콘텐츠 크리에이터',
        avatar: 'https://example.com/avatar.jpg'
      },
      searchQuery: '',
      selectedCategory: 'all',
      categories: [
        { id: 'all', name: '전체', icon: 'fas fa-th-large', count: 234 },
        { id: 'tips', name: '팁과 노하우', icon: 'fas fa-lightbulb', count: 86 },
        { id: 'review', name: 'AI 도구 리뷰', icon: 'fas fa-star', count: 45 },
        { id: 'question', name: '질문과 답변', icon: 'fas fa-question-circle', count: 67 },
        { id: 'showcase', name: '작품 공유', icon: 'fas fa-image', count: 36 }
      ],
      trendingTags: [
        { name: 'AI편집', count: 128 },
        { name: '단편영화', count: 95 },
        { name: '브이로그', count: 82 },
        { name: '미드저니', count: 76 },
        { name: '음성합성', count: 64 }
      ],
      posts: [
        {
          id: 1,
          author: {
            name: '영상편집장인',
            avatar: 'https://example.com/user1.jpg'
          },
          title: 'AI 도구로 영상 편집 시간 단축하는 꿀팁',
          excerpt: 'AI 도구를 활용하여 영상 편집 시간을 50% 이상 단축하는 방법을 공유합니다. 제가 실제로 사용하는 워크플로우와 함께...',
          category: 'tips',
          tags: ['영상편집', 'AI도구', '시간절약'],
          likes: 45,
          comments: 12,
          createdAt: '2시간 전',
          liked: false
        },
        {
          id: 2,
          author: {
            name: '테크리뷰어',
            avatar: 'https://example.com/user2.jpg'
          },
          title: '새로 나온 AI 음성 변환 도구 사용기',
          excerpt: '이번에 새로 출시된 AI 음성 변환 도구를 사용해보았습니다. 자연스러운 목소리 톤과 감정 표현이 정말 놀랍더군요...',
          category: 'review',
          tags: ['음성합성', 'AI리뷰', '더빙'],
          likes: 38,
          comments: 8,
          createdAt: '5시간 전',
          liked: true
        }
      ]
    }
  },
  computed: {
    filteredPosts() {
      return this.posts.filter(post => {
        const matchesSearch = post.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                            post.excerpt.toLowerCase().includes(this.searchQuery.toLowerCase())
        const matchesCategory = this.selectedCategory === 'all' || post.category === this.selectedCategory
        return matchesSearch && matchesCategory
      })
    }
  },
  methods: {
    selectCategory(categoryId) {
      this.selectedCategory = categoryId
    },
    getCategoryIcon(categoryId) {
      const category = this.categories.find(c => c.id === categoryId)
      return category ? category.icon : 'fas fa-th-large'
    },
    getCategoryName(categoryId) {
      const category = this.categories.find(c => c.id === categoryId)
      return category ? category.name : '기타'
    },
    toggleLike(post) {
      post.liked = !post.liked
      post.likes += post.liked ? 1 : -1
    },
    showNewPostModal() {
      // TODO: 새 게시글 작성 모달 구현
      console.log('Show new post modal')
    }
  }
}
&lt;/script>

&lt;style scoped>
.community {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.community-header {
  text-align: center;
  margin-bottom: 3rem;
}

.community-header h1 {
  font-size: 2.5rem;
  color: #1f2937;
  margin-bottom: 1rem;
}

.community-header p {
  color: #6b7280;
  font-size: 1.1rem;
}

.community-content {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 2rem;
}

.sidebar {
  background: white;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
}

.user-profile {
  text-align: center;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
  margin-bottom: 1.5rem;
}

.user-profile img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-bottom: 1rem;
}

.user-profile h3 {
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.user-profile p {
  color: #6b7280;
  font-size: 0.875rem;
}

.login-prompt {
  text-align: center;
  padding: 2rem 1rem;
  background: #f3f4f6;
  border-radius: 0.5rem;
  margin-bottom: 1.5rem;
}

.categories h3, .trending-tags h3 {
  color: #1f2937;
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

.categories ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.categories li {
  display: flex;
  align-items: center;
  padding: 0.75rem;
  color: #6b7280;
  cursor: pointer;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.categories li:hover {
  background: #f3f4f6;
  color: #1f2937;
}

.categories li.active {
  background: #6366f1;
  color: white;
}

.categories li i {
  margin-right: 0.75rem;
}

.categories li .count {
  margin-left: auto;
  background: #e5e7eb;
  padding: 0.25rem 0.5rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  color: #4b5563;
}

.categories li.active .count {
  background: rgba(255, 255, 255, 0.2);
  color: white;
}

.trending-tags {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #e5e7eb;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background: #f3f4f6;
  color: #4b5563;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}

.tag small {
  color: #9ca3af;
}

.main-content {
  min-height: 800px;
}

.content-header {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.search-box {
  flex: 1;
  position: relative;
}

.search-box input {
  width: 100%;
  padding: 0.75rem 2.5rem 0.75rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.2s;
}

.search-box input:focus {
  outline: none;
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.search-box i {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #6366f1;
  color: white;
  border: none;
  border-radius: 0.5rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary:hover {
  background: #4f46e5;
}

.post-card {
  background: white;
  border-radius: 1rem;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
}

.post-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.user-info img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.user-info h4 {
  color: #1f2937;
  margin-bottom: 0.25rem;
}

.user-info span {
  color: #6b7280;
  font-size: 0.875rem;
}

.post-category {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #f3f4f6;
  border-radius: 1rem;
  color: #4b5563;
  font-size: 0.875rem;
}

.post-content {
  margin-bottom: 1.5rem;
}

.post-content h3 {
  color: #1f2937;
  margin-bottom: 0.75rem;
  font-size: 1.25rem;
}

.post-content p {
  color: #6b7280;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.post-tags {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.post-footer {
  border-top: 1px solid #e5e7eb;
  padding-top: 1rem;
}

.interactions {
  display: flex;
  gap: 1rem;
}

.interactions button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: transparent;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  color: #6b7280;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}

.interactions button:hover {
  background: #f3f4f6;
  color: #1f2937;
}

.interactions button.active {
  background: #fee2e2;
  border-color: #fee2e2;
  color: #dc2626;
}

@media (max-width: 1024px) {
  .community-content {
    grid-template-columns: 1fr;
  }

  .sidebar {
    display: none;
  }
}

@media (max-width: 768px) {
  .community-header h1 {
    font-size: 2rem;
  }

  .content-header {
    flex-direction: column;
  }

  .new-post-btn {
    width: 100%;
    justify-content: center;
  }

  .post-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .interactions {
    justify-content: space-between;
  }

  .interactions button {
    flex: 1;
    justify-content: center;
  }
}
&lt;/style>
