<template>
  <button class="button"><IconCreate />создать</button>
</template>

<script setup lang="ts">
import IconCreate from '../icons/IconCreate.vue'
</script>

<style scoped>
.button {
  display: flex;
  align-items: center;
  gap: 8px;
  font: 600 14px/1.2 Montserrat;
  color: #0dc895;
  background: #e3fff4;
  border-radius: 50px;
  padding: 16px 32px;
  text-transform: capitalize;
  transition: 0.2s;
}

.button:hover {
  background-color: #0079c2;
  color: #fff;
}
</style>
