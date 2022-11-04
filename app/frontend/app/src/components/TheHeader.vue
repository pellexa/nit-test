<template>
  <header class="header">
    <div class="wrapper">
      <div class="logo">
        <router-link to="/" class="logo-link"><IconLogo /></router-link>
      </div>

      <nav class="nav">
        <router-link to="/" class="nav-item" :class="[path === '/deal' ? 'active' : '']">сделки</router-link>
        <router-link to="/" class="nav-item" :class="[path === '/counterparty' ? 'active' : '']">
          контрагенты
        </router-link>
        <router-link to="/" class="nav-item" :class="[path === '/report' ? 'active' : '']">отчёты</router-link>
      </nav>
    </div>
  </header>
</template>

<script setup lang="ts">
import IconLogo from './icons/IconLogo.vue'
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()
const path = computed(() => route.path)
</script>

<style scoped>
.header {
  grid-area: header;
  margin: 23px 320px 23px 320px;
}

.wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.logo {
  align-self: center;
}

.nav {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.nav-item {
  font: 600 16px/1.2 Montserrat;
  color: #0079c2;
  border: 1px solid #0079c2;
  border-radius: 50px;
  padding: 16px 32px;
  text-transform: capitalize;
  transition: 0.2s;
}

.nav-item:hover {
  background-color: #0079c2;
  color: #fff;
}

.active {
  background-color: #0079c2;
  color: #fff;
}

.nav-item.active:hover {
  background-color: #fff;
  color: #0079c2;
}
</style>
