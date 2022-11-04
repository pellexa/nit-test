<template>
  <div class="subheader">
    <slot name="title"></slot>
    <slot name="form"></slot>
  </div>
</template>
<script setup lang="ts"></script>
<style scoped>
.subheader {
  grid-area: subheader;
  height: 358px;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.138) -14.07%, rgba(0, 0, 0, 0) 41.75%),
    url('../assets/images/subheader-bg.jpg');
  background-repeat: no-repeat;
  background-size: contain;
  overflow: auto; /* prevent collapsing fields */
}
</style>
