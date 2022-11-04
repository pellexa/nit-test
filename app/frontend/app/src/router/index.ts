import { createRouter, createWebHistory } from 'vue-router'
import MainVue from '../views/MainView.vue'
import CounterpartyList from '../components/counterparty/CounterpartyList.vue'

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
  ],
})

export default router
