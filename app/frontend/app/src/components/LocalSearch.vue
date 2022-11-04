<template>
  <div class="local-search" @input="search">
    <div class="local-search-icon"><IconLocalSearch /></div>
    <input v-model="queryText" type="text" class="local-search-input" placeholder="Введите свой запрос" />
    <div class="filter-settings-icon"><IconFilterSettings /></div>
  </div>
</template>

<script setup lang="ts">
import IconLocalSearch from './icons/IconLocalSearch.vue'
import IconFilterSettings from './icons/IconFilterSettings.vue'

import { ref } from 'vue'

const queryText = ref()

function search(): void {
  console.log('Ваш запрос: ', queryText.value)
}
</script>

<style scoped>
.local-search {
  display: flex;
  align-items: center;
  gap: 6px;
  height: 52px;
  margin-left: 48px;
  background-color: #fff;
  border: 1px solid #ececec;
  border-radius: 50px;
  width: 40%;
}

.local-search-input {
  flex: 1;
  font: 400 14px / 1.2 Montserrat;
  border: none;
}

.local-search-icon {
  margin-left: 32px;
}

.filter-settings-icon {
  margin-right: 32px;
}
</style>
