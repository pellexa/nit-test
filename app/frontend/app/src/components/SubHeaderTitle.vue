<template>
  <div class="title-wrapper">
    <div class="title-name">{{ name }}</div>
    <hr class="title-line" />
    <div class="title-cross"><IconCross /></div>
  </div>
</template>

<script setup lang="ts">
import IconCross from './icons/IconCross.vue'
defineProps(['name'])
</script>

<style scoped>
.title-wrapper {
  display: flex;
  align-items: center;
}

.title-name {
  font: 300 56px/1.2 Montserrat;
  color: #fff;
  text-transform: capitalize;
}

.title-line {
  flex: 1;
  border-top: 1px solid #e1f5ff;
  margin: 0 32px 0 34px;
}
</style>
