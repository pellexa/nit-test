<template>
  <div class="form-box">
    <slot name="subheader-form"></slot>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.form-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 148px;
  background-color: #fff;
  margin: 50px 272px 0 274px;
  border-radius: 20px;
}
</style>
