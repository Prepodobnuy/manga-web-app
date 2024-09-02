<script setup>
import { RouterLink, RouterView } from 'vue-router'
import topHeader from './components/topHeader.vue'
</script>

<template>
  <topHeader />
  <header>
    <div class="wrapper">

    </div>
  </header>
  <RouterView class="router-view" />

</template>

<style scoped lang="scss">
.router-view {
  margin-top: 76px;
}
</style>
