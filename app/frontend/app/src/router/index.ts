import { createRouter, createWebHistory } from 'vue-router'
import MainVue from '../views/MainView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainVue,
    },
  ],
})

export default router
