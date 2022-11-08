<template>
  <button class="button"><IconCreate class="icon-create" />создать</button>
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
  color: #b3b3b3;
  background: #f7f7f7;
  border-radius: 50px;
  padding: 16px 32px;
  text-transform: capitalize;
  transition: 0.2s;
}

.button:hover {
  color: #0dc895;
  background: #e3fff4;
}

.icon-create {
  transition: 0.2s;
}

.button:hover .icon-create {
  fill: #0dc895;
}
</style>
