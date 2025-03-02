&lt;template>
  &lt;div class="tools">
    &lt;div class="tools-header">
      &lt;h1>AI 도구 모음&lt;/h1>
      &lt;div class="search-box">
        &lt;input type="text" v-model="searchQuery" placeholder="AI 도구 검색...">
        &lt;i class="fas fa-search">&lt;/i>
      &lt;/div>
      &lt;div class="category-filters">
        &lt;button 
          v-for="category in categories" 
          :key="category.id"
          :class="['category-btn', { active: selectedCategory === category.id }]"
          @click="selectedCategory = category.id"
        >
          &lt;i :class="category.icon">&lt;/i> {{ category.name }}
        &lt;/button>
      &lt;/div>
    &lt;/div>

    &lt;div class="tools-grid">
      &lt;div v-for="tool in filteredTools" :key="tool.id" class="tool-card">
        &lt;div class="tool-header">
          &lt;img :src="tool.logo" :alt="tool.name">
          &lt;div class="tool-badges">
            &lt;span v-if="tool.free" class="badge free">무료&lt;/span>
            &lt;span v-if="tool.popular" class="badge popular">인기&lt;/span>
          &lt;/div>
        &lt;/div>
        &lt;h3>{{ tool.name }}&lt;/h3>
        &lt;p>{{ tool.description }}&lt;/p>
        &lt;div class="tool-tags">
          &lt;span v-for="tag in tool.tags" :key="tag" class="tag">{{ tag }}&lt;/span>
        &lt;/div>
        &lt;div class="tool-actions">
          &lt;a :href="tool.url" target="_blank" class="btn btn-primary">
            &lt;i class="fas fa-external-link-alt">&lt;/i> 사용하기
          &lt;/a>
          &lt;button class="btn btn-secondary" @click="showTutorial(tool)">
            &lt;i class="fas fa-book">&lt;/i> 튜토리얼
          &lt;/button>
        &lt;/div>
      &lt;/div>
    &lt;/div>
  &lt;/div>
&lt;/template>

&lt;script>
export default {
  name: 'ToolsView',
  data() {
    return {
      searchQuery: '',
      selectedCategory: 'all',
      categories: [
        { id: 'all', name: '전체', icon: 'fas fa-th-large' },
        { id: 'video', name: '동영상', icon: 'fas fa-video' },
        { id: 'image', name: '이미지', icon: 'fas fa-image' },
        { id: 'audio', name: '음성/더빙', icon: 'fas fa-microphone' },
        { id: 'writing', name: '글쓰기', icon: 'fas fa-pen' },
        { id: 'editing', name: '편집', icon: 'fas fa-cut' }
      ],
      tools: [
        {
          id: 1,
          name: 'Runway ML',
          description: '인공지능 기반 비디오 편집 및 특수효과 도구',
          category: 'video',
          logo: 'https://example.com/runway.png',
          url: 'https://runway.ml',
          tags: ['동영상 편집', 'AI 효과', '특수효과'],
          free: true,
          popular: true
        },
        {
          id: 2,
          name: 'Midjourney',
          description: '텍스트를 입력하면 고품질 이미지를 생성하는 AI',
          category: 'image',
          logo: 'https://example.com/midjourney.png',
          url: 'https://www.midjourney.com',
          tags: ['이미지 생성', '아트', 'Discord'],
          free: false,
          popular: true
        },
        {
          id: 3,
          name: 'ElevenLabs',
          description: '자연스러운 AI 음성 생성 및 더빙 도구',
          category: 'audio',
          logo: 'https://example.com/elevenlabs.png',
          url: 'https://elevenlabs.io',
          tags: ['음성 합성', '더빙', '다국어'],
          free: true,
          popular: false
        }
        // 더 많은 도구들...
      ]
    }
  },
  computed: {
    filteredTools() {
      return this.tools.filter(tool => {
        const matchesSearch = tool.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                            tool.description.toLowerCase().includes(this.searchQuery.toLowerCase())
        const matchesCategory = this.selectedCategory === 'all' || tool.category === this.selectedCategory
        return matchesSearch && matchesCategory
      })
    }
  },
  methods: {
    showTutorial(tool) {
      // TODO: 튜토리얼 모달 구현
      console.log('Show tutorial for:', tool.name)
    }
  }
}
&lt;/script>

&lt;style scoped>
.tools {
  max-width: 1200px;
  margin: 0 auto;
}

.tools-header {
  text-align: center;
  margin-bottom: 3rem;
}

.tools-header h1 {
  font-size: 2.5rem;
  color: #1f2937;
  margin-bottom: 1.5rem;
}

.search-box {
  position: relative;
  max-width: 500px;
  margin: 0 auto 2rem;
}

.search-box input {
  width: 100%;
  padding: 1rem 3rem 1rem 1.5rem;
  border: 2px solid #e5e7eb;
  border-radius: 0.75rem;
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

.category-filters {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.category-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border: none;
  border-radius: 0.5rem;
  background: #f3f4f6;
  color: #6b7280;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.category-btn:hover {
  background: #e5e7eb;
  color: #1f2937;
}

.category-btn.active {
  background: #6366f1;
  color: white;
}

.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  padding: 2rem 0;
}

.tool-card {
  background: white;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
  transition: transform 0.2s;
}

.tool-card:hover {
  transform: translateY(-5px);
}

.tool-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.tool-header img {
  width: 48px;
  height: 48px;
  border-radius: 0.5rem;
}

.tool-badges {
  display: flex;
  gap: 0.5rem;
}

.badge {
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 500;
}

.badge.free {
  background: #dcfce7;
  color: #15803d;
}

.badge.popular {
  background: #fee2e2;
  color: #b91c1c;
}

.tool-card h3 {
  font-size: 1.25rem;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.tool-card p {
  color: #6b7280;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.tool-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.tag {
  background: #f3f4f6;
  color: #4b5563;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
}

.tool-actions {
  display: flex;
  gap: 1rem;
}

.btn {
  flex: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem;
  border-radius: 0.5rem;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.2s;
}

.btn-primary {
  background: #6366f1;
  color: white;
  border: none;
}

.btn-primary:hover {
  background: #4f46e5;
}

.btn-secondary {
  background: white;
  color: #6b7280;
  border: 1px solid #e5e7eb;
}

.btn-secondary:hover {
  background: #f3f4f6;
}

@media (max-width: 768px) {
  .tools-header h1 {
    font-size: 2rem;
  }

  .category-filters {
    gap: 0.5rem;
  }

  .category-btn {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
  }

  .tools-grid {
    grid-template-columns: 1fr;
  }
}
&lt;/style>
