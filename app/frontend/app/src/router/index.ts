import { createRouter, createWebHistory } from 'vue-router'
import MainVue from '../views/MainView.vue'
import CounterpartyList from '../components/counterparty/CounterpartyList.vue'
import DealList from '@/components/deal/DealList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainVue,
    },

    {
      path: '/counterparty',
      name: 'counterparty',
      component: CounterpartyList,
    },

    {
      path: '/deal',
      name: 'deal',
      component: DealList,
    },
  ],
})

export default router
