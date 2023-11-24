<script setup>
import BaseHeader from "./components/layout/BaseHeader.vue";
import GantChart from "./components/GantChart.vue";

const changePage = (pageIndex) => {

}
</script>

<template>
    <BaseHeader @page-chosen="changePage"/>

    <GantChart/>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
