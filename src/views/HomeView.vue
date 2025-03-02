&lt;template>
  &lt;div class="home">
    &lt;section class="hero">
      &lt;div class="hero-content">
        &lt;h1>AI로 더 쉽게 &lt;br>콘텐츠를 만들어보세요&lt;/h1>
        &lt;p>유튜버, 인플루언서, 블로거를 위한 최고의 AI 도구 모음&lt;/p>
        &lt;div class="hero-buttons">
          &lt;router-link to="/tools" class="btn btn-primary">
            &lt;i class="fas fa-tools">&lt;/i> AI 도구 살펴보기
          &lt;/router-link>
          &lt;router-link to="/try-ai" class="btn btn-secondary">
            &lt;i class="fas fa-magic">&lt;/i> AI 체험하기
          &lt;/router-link>
        &lt;/div>
      &lt;/div>
    &lt;/section>

    &lt;section class="features">
      &lt;h2>주요 기능&lt;/h2>
      &lt;div class="features-grid">
        &lt;div class="feature-card">
          &lt;i class="fas fa-tools">&lt;/i>
          &lt;h3>AI 도구 모음&lt;/h3>
          &lt;p>200+ 크리에이터를 위한 AI 도구와 상세한 사용 가이드&lt;/p>
        &lt;/div>
        
        &lt;div class="feature-card">
          &lt;i class="fab fa-youtube">&lt;/i>
          &lt;h3>유튜브 분석&lt;/h3>
          &lt;p>영상 URL을 입력하면 사용된 AI 도구를 자동으로 찾아드려요&lt;/p>
        &lt;/div>
        
        &lt;div class="feature-card">
          &lt;i class="fas fa-magic">&lt;/i>
          &lt;h3>AI 체험&lt;/h3>
          &lt;p>다양한 AI 도구를 웹에서 바로 체험해보세요&lt;/p>
        &lt;/div>
        
        &lt;div class="feature-card">
          &lt;i class="fas fa-users">&lt;/i>
          &lt;h3>크리에이터 커뮤니티&lt;/h3>
          &lt;p>다른 크리에이터와 AI 활용 노하우를 공유하세요&lt;/p>
        &lt;/div>
      &lt;/div>
    &lt;/section>

    &lt;section class="cta">
      &lt;div class="cta-content">
        &lt;h2>프리미엄 멤버가 되어보세요&lt;/h2>
        &lt;p>고급 AI 튜토리얼과 전문가 가이드로 콘텐츠 제작 실력을 향상시켜보세요&lt;/p>
        &lt;router-link to="/premium" class="btn btn-premium">
          &lt;i class="fas fa-crown">&lt;/i> 프리미엄 시작하기
        &lt;/router-link>
      &lt;/div>
    &lt;/section>
  &lt;/div>
&lt;/template>

&lt;script>
export default {
  name: 'HomeView'
}
&lt;/script>

&lt;style scoped>
.hero {
  background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
  color: white;
  padding: 4rem 2rem;
  text-align: center;
  border-radius: 1rem;
  margin-bottom: 4rem;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.hero p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.2s;
}

.btn-primary {
  background: white;
  color: #6366f1;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.2);
}

.features {
  padding: 4rem 0;
}

.features h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 3rem;
  color: #1f2937;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
  transition: transform 0.2s;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-card i {
  font-size: 2.5rem;
  color: #6366f1;
  margin-bottom: 1.5rem;
}

.feature-card h3 {
  font-size: 1.25rem;
  margin-bottom: 1rem;
  color: #1f2937;
}

.feature-card p {
  color: #6b7280;
}

.cta {
  background: #1f2937;
  color: white;
  padding: 4rem 2rem;
  border-radius: 1rem;
  margin-top: 4rem;
}

.cta-content {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

.cta h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.cta p {
  margin-bottom: 2rem;
  opacity: 0.9;
}

.btn-premium {
  background: #f59e0b;
  color: white;
}

.btn-premium:hover {
  background: #d97706;
}

@media (max-width: 768px) {
  .hero {
    padding: 3rem 1rem;
  }

  .hero h1 {
    font-size: 2rem;
  }

  .hero p {
    font-size: 1rem;
  }

  .hero-buttons {
    flex-direction: column;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }
}
&lt;/style>
