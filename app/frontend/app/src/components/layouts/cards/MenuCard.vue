<template>
  <div class="card">
    <div class="card-title">{{ title }}</div>

    <div class="menu-wrapper">
      <div class="menu-items-wrapper"><slot name="menu-items"></slot></div>
      <div class="card-icon-wrapper"><slot name="card-icon"></slot></div>
    </div>
    <slot name="button"></slot>
  </div>
</template>

<script setup lang="ts">
defineProps(['title'])
</script>

<style scoped>
.card {
  position: relative;
  height: 535px;
  width: 411px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 3px 4px 15px -10px rgba(0, 110, 189, 0.2), 0px 1px 30px -3px rgba(0, 78, 135, 0.12);
}

.card-title {
  font: 400 28px/1.5 Montserrat;
  color: #1e2832;
  padding: 48px 0 38px 48px;
}

.card-title::first-letter {
  text-transform: uppercase;
}

.menu-wrapper {
  display: grid;
  grid-template-columns: auto 122px;
}

.card-icon-wrapper {
  align-self: center;
}
</style>
