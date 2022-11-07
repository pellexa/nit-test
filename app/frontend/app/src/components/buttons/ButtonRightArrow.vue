<template>
  <button class="button">
    {{ title }}
    <div class="wrapper-icon">
      <IconRightArrow />
    </div>
  </button>
</template>

<script setup lang="ts">
import IconRightArrow from '../icons/cards/IconRightArrow.vue'

defineProps(['title'])
</script>

<style scoped>
.button {
  position: absolute;
  right: 48px;
  bottom: 48px;
  display: flex;
  gap: 14px;
  font: 600 16px/1.5 Montserrat;
  color: #fff;
  background: #0079c2;
  border-radius: 50px;
  padding: 14px 0 14px 34px;
  text-transform: capitalize;
  transition: 0.2s;
}

.button:hover .wrapper-icon {
  transform: translate(7px, 0);
}

.wrapper-icon {
  padding-right: 32px;
  transition: 0.2s;
}
</style>
