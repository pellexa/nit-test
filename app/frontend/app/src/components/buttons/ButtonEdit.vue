<template>
  <button class="button"><IconEdit class="icon-edit" />реадктировать</button>
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
  color: #0079c2;
  background: #f2f7fc;
}

.icon-edit {
  transition: 0.2s;
}

.button:hover .icon-edit {
  fill: #0079c2;
}
</style>
