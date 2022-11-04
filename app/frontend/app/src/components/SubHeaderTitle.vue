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
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
}

.title-name {
  font: 300 56px/1.2 Montserrat;
  color: #fff;
  text-transform: capitalize;
}

.title-line {
  border-top: 1px solid #e1f5ff;
  /* align-self: center; */
  margin: 0 32px 0 34px;
  transform: translate(0 2px);
}
</style>
