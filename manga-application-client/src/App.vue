<script setup>
import { RouterLink, RouterView } from 'vue-router'
import topHeader from './components/topHeader.vue'
import topFooter from './components/topFooter.vue';
</script>

<template>
  <div class="wrapper">
    <topHeader />
    <RouterView class="router-view" />
  </div>
  <topFooter />
</template>

<style scoped lang="scss">
.router-view {
  margin-top: 76px;
}

.wrapper {
  min-height: 100vh;
}
</style>
