<template>
  <footer class="footer">
    <address>
      <div class="author-title">автор проекта</div>
      <div class="author-name">сергей пудов</div>
      <div class="phone-wrapper">
        <IconPhone />
        <div class="phone-title">телефон</div>
        <div class="phone-value">+12345678901</div>
      </div>

      <div class="email-wrapper">
        <IconEmail />
        <div class="email-title">e-mail</div>
        <div class="email-value">test@test.test</div>
      </div>
    </address>
  </footer>
</template>

<script setup lang="ts">
import IconPhone from './icons/IconPhone.vue'
import IconEmail from './icons/IconEmail.vue'
</script>

<style scoped>
.footer {
  font: 400 14px/1.5 Montserrat;
  height: 274px;
  background-color: #fff;
  padding: 72px 320px 0;
}

address {
  display: inline-block;
}

.author-title::first-letter {
  text-transform: uppercase;
}

.author-name {
  text-transform: capitalize;
}

.phone-wrapper {
  display: flex;
  gap: 7px;
  align-items: center;
  padding-top: 36px;
}

.phone-title {
  text-transform: capitalize;
}

.email-wrapper {
  display: flex;
  gap: 7px;
  align-items: center;
  padding-top: 3px;
}

.email-title::first-letter {
  text-transform: uppercase;
}
</style>
