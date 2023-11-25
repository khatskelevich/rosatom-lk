<script setup>
const emit = defineEmits(['pageChosen'])
const props = defineProps(['currentPage'])

const goTo = (pageIndex) => {
    emit('pageChosen', pageIndex)
}
</script>

<template>
    <el-menu
        class="el-menu-demo"
        mode="horizontal"
        :default-active="1"
    >
        <div class="logo-container">
            <img class="logo" src="/rosatomlogo.png">
        </div>
        <el-menu-item index="0" @click="goTo(0)">Временная шкала</el-menu-item>
        <el-menu-item index="1" @click="goTo(1)">Загрузить данные</el-menu-item>
        <el-menu-item index="2" @click="goTo(2)">Дашборд</el-menu-item>
    </el-menu>
</template>

<style scoped>
.logo-container {
    display: flex;
    align-items: center;
    margin: 0 20px;
}

.logo {
    height: 20px;
    line-height: 59px;
}
</style>
