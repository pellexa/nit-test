<template>
  <TheHeader />
  <SubHeader>
    <template v-slot:form><TheSearch class="main-search" /></template>
  </SubHeader>
</template>

<script setup lang="ts">
import TheHeader from '../components/TheHeader.vue'
import SubHeader from '../components/SubHeader.vue'
import TheSearch from '../components/TheSearch.vue'
</script>

<style scoped>
.main-search {
  margin: 66px 320px 0;
}
</style>
