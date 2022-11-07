<template>
  <div class="item-wrapper">
    <div class="item-icon-wrapper">
      <slot></slot>
    </div>
    <div class="title">{{ title }}</div>
  </div>
</template>

<script setup lang="ts">
defineProps(['title'])
</script>

<style scoped>
.item-wrapper {
  display: flex;
  gap: 18px;
  padding: 18px 21px 18px 48px;
  align-items: center;
}

.title {
  font: 400 18px/1.4 Montserrat;
  color: #46555f;
}

.title::first-letter {
  text-transform: uppercase;
}
</style>
