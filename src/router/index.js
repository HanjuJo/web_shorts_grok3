import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ToolsView from '../views/ToolsView.vue'
import YoutubeAnalyzerView from '../views/YoutubeAnalyzerView.vue'
import TryAiView from '../views/TryAiView.vue'
import CommunityView from '../views/CommunityView.vue'
import PremiumView from '../views/PremiumView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/tools',
    name: 'tools',
    component: ToolsView
  },
  {
    path: '/youtube-analyzer',
    name: 'youtube-analyzer',
    component: YoutubeAnalyzerView
  },
  {
    path: '/try-ai',
    name: 'try-ai',
    component: TryAiView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/premium',
    name: 'premium',
    component: PremiumView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
