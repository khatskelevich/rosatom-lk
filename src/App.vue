<script setup>
import {ref} from 'vue'
import BaseHeader from "./components/layout/BaseHeader.vue";
import GantChart from "./components/GantChart.vue";
import TimelineChart from "./components/TimelineChart.vue";
import UploadForm from "./components/UploadForm.vue";

let currentIndex = ref(0)
const changePage = (pageIndex) => {
    currentIndex.value = pageIndex
}

const components = [TimelineChart, UploadForm]
</script>

<template>
    <el-header>
        <BaseHeader
                @page-chosen="changePage"
                :current-page="currentIndex"
        />
    </el-header>

    <el-main>
        <component :is="components[currentIndex]"></component>
    </el-main>
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
