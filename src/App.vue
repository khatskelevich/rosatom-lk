<script setup>
import {ref} from 'vue'
import BaseHeader from "./components/layout/BaseHeader.vue";
import GantChart from "./components/GantChart.vue";
import TimelineChart from "./components/TimelineChart.vue";
import UploadForm from "./components/UploadForm.vue";
import Statistic from "./components/Statistic.vue";

let currentIndex = ref(0)
const changePage = (pageIndex) => {
    currentIndex.value = pageIndex
}

const components = [TimelineChart, UploadForm, Statistic]
</script>

<template>
    <el-header>
        <BaseHeader
                @page-chosen="changePage"
                :current-page="currentIndex"
        />
    </el-header>

    <el-main class="rs-main">
        <component :is="components[currentIndex]"></component>
    </el-main>
</template>

<style scoped>
.rs-main {
    min-height: calc(100vh - 60px);
}
</style>
