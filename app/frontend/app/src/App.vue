<template>
  <RouterView />
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<style>
/**
 * The global styles are here and in the scr/assets/reset.css file.
 */
@font-face {
  font-family: Montserrat;
  font-style: normal;
  font-weight: 300;
  src: url('./assets/fonts/Montserrat/Montserrat-Light.woff2') format('woff2'),
    url('./assets/fonts/Montserrat/Montserrat-Light.woff') format('woff'),
    url('./assets/fonts/Montserrat/Montserrat-Light.ttf') format('ttf'),
    url('./assets/fonts/Montserrat/Montserrat-Light.eot') format('eot');
}

@font-face {
  font-family: Montserrat;
  font-style: normal;
  font-weight: normal; /* 400 */
  src: url('./assets/fonts/Montserrat/Montserrat-Regular.woff2') format('woff2'),
    url('./assets/fonts/Montserrat/Montserrat-Regular.woff') format('woff'),
    url('./assets/fonts/Montserrat/Montserrat-Regular.ttf') format('ttf'),
    url('./assets/fonts/Montserrat/Montserrat-Regular.eot') format('eot');
}

@font-face {
  font-family: Montserrat;
  font-style: normal;
  font-weight: medium; /* 500 */
  src: url('./assets/fonts/Montserrat/Montserrat-Medium.woff2') format('woff2'),
    url('./assets/fonts/Montserrat/Montserrat-Medium.woff') format('woff'),
    url('./assets/fonts/Montserrat/Montserrat-Medium.ttf') format('ttf'),
    url('./assets/fonts/Montserrat/Montserrat-Medium.eot') format('eot');
}

@font-face {
  font-family: Montserrat;
  font-style: normal;
  font-weight: 600;
  src: url('./assets/fonts/Montserrat/Montserrat-SemiBold.woff2') format('woff2'),
    url('./assets/fonts/Montserrat/Montserrat-SemiBold.woff') format('woff'),
    url('./assets/fonts/Montserrat/Montserrat-SemiBold.ttf') format('ttf'),
    url('./assets/fonts/Montserrat/Montserrat-SemiBold.eot') format('eot');
}

@font-face {
  font-family: Montserrat;
  font-style: normal;
  font-weight: bold; /* 700 */
  src: url('./assets/fonts/Montserrat/Montserrat-Bold.woff2') format('woff2'),
    url('./assets/fonts/Montserrat/Montserrat-Bold.woff') format('woff'),
    url('./assets/fonts/Montserrat/Montserrat-Bold.ttf') format('ttf'),
    url('./assets/fonts/Montserrat/Montserrat-Bold.eot') format('eot');
}

/**
 * General global styles.
 */
:root {
  font: 400 14px/1.2 Montserrat;
  box-sizing: border-box;
}

*,
::before,
::after {
  box-sizing: inherit;
}

/**
 * Links and buttons.
 */
a,
.button {
  cursor: pointer;
  outline: none;
  white-space: nowrap;
  transition: 0.2s;
}

a {
  text-decoration: none;
}

.button {
  background-color: transparent;
  border: none;
}

a:hover,
.button:hover {
  text-shadow: 0 0 0.05em;
}
</style>
