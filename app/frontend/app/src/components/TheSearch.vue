<template>
  <form class="search" @submit.prevent="search">
    <div class="search-icon"><IconSearch /></div>
    <input v-model="searchText" type="text" name="search" class="search-input" placeholder="Что будем искать?" />
    <button type="submit" class="button">найти</button>
  </form>
</template>

<script setup lang="ts">
import IconSearch from './icons/IconSearch.vue'

import { ref } from 'vue'

const searchText = ref()

function search(): void {
  console.log('Вы искали: ', searchText.value)
}
</script>

<style scoped>
.search {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 16px;
  height: 84px;
  align-content: center;
  background: linear-gradient(180deg, #e1f5ff 10.94%, #bee6ff 72.4%);
  box-shadow: 3px 4px 15px -10px rgba(0, 110, 189, 0.2), 0px 1px 30px -3px rgba(0, 78, 135, 0.12);
  border-radius: 50px;
}

.search-icon {
  align-self: center;
  margin: 0 0 0 26px;
}

.search-input {
  font: 400 16px/1.25 Montserrat;
  height: 52px;
  background: #fafafa;
  border-radius: 50px;
  padding: 16px 32px;
}

.search-input::placeholder {
  color: #afb9be;
}

.button {
  font: 600 16px/1.25 Montserrat;
  color: #fff;
  background-color: #0079c2;
  border: 1px solid #0079c2;
  border-radius: 50px;
  padding: 16px 40.5px;
  text-transform: capitalize;
  transition: 0.2s;
  margin-right: 16px;
}

.button:hover {
  background-color: transparent;
  color: #0079c2;
}
</style>
