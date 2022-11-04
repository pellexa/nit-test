<template>
  <button class="button"><IconEdit />реадктировать</button>
</template>

<script setup lang="ts">
import IconEdit from '../icons/IconEdit.vue'
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
  background-color: #0079c2;
  color: #fff;
}
</style>
