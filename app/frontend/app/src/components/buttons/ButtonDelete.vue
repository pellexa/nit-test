<template>
  <button class="button"><IconDelete class="icon-delete" />удалить</button>
</template>

<script setup lang="ts">
import IconDelete from '../icons/IconDelete.vue'
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
  color: #fc6770;
  background: #fff5f5;
}

.icon-delete {
  transition: 0.2s;
}

.button:hover .icon-delete {
  fill: #fc6770;
}
</style>
