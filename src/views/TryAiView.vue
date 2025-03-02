&lt;template>
  &lt;div class="try-ai">
    &lt;div class="try-ai-header">
      &lt;h1>AI 도구 체험하기&lt;/h1>
      &lt;p>다양한 AI 도구를 직접 체험해보세요&lt;/p>
    &lt;/div>

    &lt;div class="ai-tools-container">
      &lt;div class="tools-nav">
        &lt;button 
          v-for="tool in aiTools" 
          :key="tool.id"
          :class="['tool-nav-btn', { active: selectedTool === tool.id }]"
          @click="selectTool(tool.id)"
        >
          &lt;i :class="tool.icon">&lt;/i>
          &lt;span>{{ tool.name }}&lt;/span>
        &lt;/button>
      &lt;/div>

      &lt;div class="tool-workspace">
        &lt;div class="tool-header">
          &lt;h2>{{ currentTool.name }}&lt;/h2>
          &lt;p>{{ currentTool.description }}&lt;/p>
        &lt;/div>

        &lt;div class="tool-interface">
          &lt;!-- 이미지 생성 도구 -->
          &lt;div v-if="selectedTool === 'image-generator'" class="image-generator">
            &lt;div class="input-section">
              &lt;textarea 
                v-model="imagePrompt"
                placeholder="이미지를 설명해주세요..."
                rows="4"
              >&lt;/textarea>
              &lt;div class="options">
                &lt;select v-model="imageStyle">
                  &lt;option value="realistic">사실적&lt;/option>
                  &lt;option value="artistic">예술적&lt;/option>
                  &lt;option value="cartoon">만화&lt;/option>
                &lt;/select>
                &lt;select v-model="imageSize">
                  &lt;option value="512x512">512x512&lt;/option>
                  &lt;option value="1024x1024">1024x1024&lt;/option>
                &lt;/select>
              &lt;/div>
              &lt;button @click="generateImage" :disabled="!imagePrompt || loading">
                &lt;i class="fas fa-magic" v-if="!loading">&lt;/i>
                &lt;i class="fas fa-spinner fa-spin" v-else>&lt;/i>
                이미지 생성
              &lt;/button>
            &lt;/div>
            &lt;div class="result-section" v-if="generatedImage">
              &lt;img :src="generatedImage" alt="Generated image">
              &lt;button class="download-btn">
                &lt;i class="fas fa-download">&lt;/i> 다운로드
              &lt;/button>
            &lt;/div>
          &lt;/div>

          &lt;!-- 텍스트 생성 도구 -->
          &lt;div v-if="selectedTool === 'text-generator'" class="text-generator">
            &lt;div class="input-section">
              &lt;textarea 
                v-model="textPrompt"
                placeholder="어떤 내용의 텍스트를 생성할까요?"
                rows="4"
              >&lt;/textarea>
              &lt;div class="options">
                &lt;select v-model="textType">
                  &lt;option value="blog">블로그 포스트&lt;/option>
                  &lt;option value="script">영상 스크립트&lt;/option>
                  &lt;option value="social">소셜미디어 포스트&lt;/option>
                &lt;/select>
                &lt;select v-model="textLength">
                  &lt;option value="short">짧게 (300자)&lt;/option>
                  &lt;option value="medium">중간 (1000자)&lt;/option>
                  &lt;option value="long">길게 (2000자)&lt;/option>
                &lt;/select>
              &lt;/div>
              &lt;button @click="generateText" :disabled="!textPrompt || loading">
                &lt;i class="fas fa-pen-fancy" v-if="!loading">&lt;/i>
                &lt;i class="fas fa-spinner fa-spin" v-else>&lt;/i>
                텍스트 생성
              &lt;/button>
            &lt;/div>
            &lt;div class="result-section" v-if="generatedText">
              &lt;div class="text-result">
                &lt;p>{{ generatedText }}&lt;/p>
              &lt;/div>
              &lt;button class="copy-btn" @click="copyText">
                &lt;i class="fas fa-copy">&lt;/i> 복사하기
              &lt;/button>
            &lt;/div>
          &lt;/div>

          &lt;!-- 음성 생성 도구 -->
          &lt;div v-if="selectedTool === 'voice-generator'" class="voice-generator">
            &lt;div class="input-section">
              &lt;textarea 
                v-model="voiceText"
                placeholder="음성으로 변환할 텍스트를 입력하세요..."
                rows="4"
              >&lt;/textarea>
              &lt;div class="options">
                &lt;select v-model="voiceType">
                  &lt;option value="male1">남성 목소리 1&lt;/option>
                  &lt;option value="female1">여성 목소리 1&lt;/option>
                  &lt;option value="male2">남성 목소리 2&lt;/option>
                  &lt;option value="female2">여성 목소리 2&lt;/option>
                &lt;/select>
                &lt;select v-model="voiceLanguage">
                  &lt;option value="ko">한국어&lt;/option>
                  &lt;option value="en">영어&lt;/option>
                  &lt;option value="ja">일본어&lt;/option>
                &lt;/select>
              &lt;/div>
              &lt;button @click="generateVoice" :disabled="!voiceText || loading">
                &lt;i class="fas fa-microphone" v-if="!loading">&lt;/i>
                &lt;i class="fas fa-spinner fa-spin" v-else>&lt;/i>
                음성 생성
              &lt;/button>
            &lt;/div>
            &lt;div class="result-section" v-if="generatedVoice">
              &lt;audio controls :src="generatedVoice">&lt;/audio>
              &lt;button class="download-btn">
                &lt;i class="fas fa-download">&lt;/i> 다운로드
              &lt;/button>
            &lt;/div>
          &lt;/div>
        &lt;/div>
      &lt;/div>
    &lt;/div>
  &lt;/div>
&lt;/template>

&lt;script>
export default {
  name: 'TryAiView',
  data() {
    return {
      selectedTool: 'image-generator',
      loading: false,
      aiTools: [
        {
          id: 'image-generator',
          name: '이미지 생성',
          icon: 'fas fa-image',
          description: 'AI가 텍스트 설명을 바탕으로 이미지를 생성합니다'
        },
        {
          id: 'text-generator',
          name: '텍스트 생성',
          icon: 'fas fa-pen-fancy',
          description: '블로그 포스트, 영상 스크립트 등 다양한 텍스트를 생성합니다'
        },
        {
          id: 'voice-generator',
          name: '음성 생성',
          icon: 'fas fa-microphone',
          description: '자연스러운 AI 음성을 생성합니다'
        }
      ],
      // 이미지 생성 관련 상태
      imagePrompt: '',
      imageStyle: 'realistic',
      imageSize: '512x512',
      generatedImage: null,
      
      // 텍스트 생성 관련 상태
      textPrompt: '',
      textType: 'blog',
      textLength: 'medium',
      generatedText: null,
      
      // 음성 생성 관련 상태
      voiceText: '',
      voiceType: 'female1',
      voiceLanguage: 'ko',
      generatedVoice: null
    }
  },
  computed: {
    currentTool() {
      return this.aiTools.find(tool => tool.id === this.selectedTool)
    }
  },
  methods: {
    selectTool(toolId) {
      this.selectedTool = toolId
      this.resetStates()
    },
    resetStates() {
      this.imagePrompt = ''
      this.textPrompt = ''
      this.voiceText = ''
      this.generatedImage = null
      this.generatedText = null
      this.generatedVoice = null
    },
    async generateImage() {
      this.loading = true
      try {
        // TODO: 실제 API 연동
        await new Promise(resolve => setTimeout(resolve, 2000))
        this.generatedImage = 'https://example.com/generated-image.jpg'
      } catch (error) {
        console.error('Image generation error:', error)
      } finally {
        this.loading = false
      }
    },
    async generateText() {
      this.loading = true
      try {
        // TODO: 실제 API 연동
        await new Promise(resolve => setTimeout(resolve, 1500))
        this.generatedText = '생성된 텍스트가 여기에 표시됩니다...'
      } catch (error) {
        console.error('Text generation error:', error)
      } finally {
        this.loading = false
      }
    },
    async generateVoice() {
      this.loading = true
      try {
        // TODO: 실제 API 연동
        await new Promise(resolve => setTimeout(resolve, 1500))
        this.generatedVoice = 'https://example.com/generated-voice.mp3'
      } catch (error) {
        console.error('Voice generation error:', error)
      } finally {
        this.loading = false
      }
    },
    copyText() {
      if (this.generatedText) {
        navigator.clipboard.writeText(this.generatedText)
          .then(() => {
            // TODO: 복사 성공 알림
          })
          .catch(err => {
            console.error('Failed to copy text:', err)
          })
      }
    }
  }
}
&lt;/script>

&lt;style scoped>
.try-ai {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.try-ai-header {
  text-align: center;
  margin-bottom: 3rem;
}

.try-ai-header h1 {
  font-size: 2.5rem;
  color: #1f2937;
  margin-bottom: 1rem;
}

.try-ai-header p {
  color: #6b7280;
  font-size: 1.1rem;
}

.ai-tools-container {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 2rem;
  background: white;
  border-radius: 1rem;
  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
  overflow: hidden;
}

.tools-nav {
  background: #f3f4f6;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.tool-nav-btn {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border: none;
  border-radius: 0.5rem;
  background: transparent;
  color: #6b7280;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  text-align: left;
}

.tool-nav-btn:hover {
  background: #e5e7eb;
  color: #1f2937;
}

.tool-nav-btn.active {
  background: #6366f1;
  color: white;
}

.tool-workspace {
  padding: 2rem;
}

.tool-header {
  margin-bottom: 2rem;
}

.tool-header h2 {
  font-size: 1.5rem;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.tool-header p {
  color: #6b7280;
}

.tool-interface {
  background: #f9fafb;
  border-radius: 0.75rem;
  padding: 1.5rem;
}

.input-section {
  margin-bottom: 2rem;
}

textarea {
  width: 100%;
  padding: 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 0.5rem;
  font-size: 1rem;
  resize: vertical;
  transition: all 0.2s;
}

textarea:focus {
  outline: none;
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.options {
  display: flex;
  gap: 1rem;
  margin: 1rem 0;
}

select {
  padding: 0.5rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  background: white;
  color: #1f2937;
  font-size: 0.875rem;
}

button {
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

button:hover:not(:disabled) {
  background: #4f46e5;
}

button:disabled {
  background: #9ca3af;
  cursor: not-allowed;
}

.result-section {
  background: white;
  border-radius: 0.5rem;
  padding: 1.5rem;
  box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
}

.result-section img {
  width: 100%;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
}

.text-result {
  max-height: 300px;
  overflow-y: auto;
  padding: 1rem;
  background: #f3f4f6;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
}

.text-result p {
  white-space: pre-wrap;
  color: #1f2937;
  line-height: 1.6;
}

audio {
  width: 100%;
  margin-bottom: 1rem;
}

.download-btn, .copy-btn {
  width: 100%;
  justify-content: center;
  background: #4b5563;
}

.download-btn:hover, .copy-btn:hover {
  background: #374151;
}

@media (max-width: 768px) {
  .try-ai-header h1 {
    font-size: 2rem;
  }

  .ai-tools-container {
    grid-template-columns: 1fr;
  }

  .tools-nav {
    padding: 1rem;
  }

  .tool-workspace {
    padding: 1rem;
  }

  .options {
    flex-direction: column;
  }

  select {
    width: 100%;
  }
}
&lt;/style>
