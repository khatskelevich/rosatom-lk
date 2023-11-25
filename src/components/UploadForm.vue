<script setup>
import {genFileId} from 'element-plus'
import {ref} from 'vue'
import {UploadFilled} from '@element-plus/icons-vue'

const upload = ref()

const handleExceed = (files) => {
    upload.value.clearFiles()
    const file = files[0]
    file.uid = genFileId()
    upload.value.handleStart(file)
}

const submitUpload = () => {
    upload.value.submit()
}

</script>
<template>
    <el-steps :space="200" :active="1" finish-status="success" class="steps">
        <el-step title="Файл получен" />
        <el-step title="Обрабатывается" />
        <el-step title="Готово" />
    </el-steps>

    <el-upload
            ref="upload"
            class="upload-form"
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            drag
    >
        <el-icon class="el-icon--upload">
            <upload-filled/>
        </el-icon>
        <div class="el-upload__text">
            Перетащите файл сюда или <em>кликните для загрузки</em>
        </div>
        <template #tip>
            <div class="el-upload__tip text-red">
                лимит в 1 файл, новый файл перетрёт уже загруженный
            </div>
        </template>
    </el-upload>
</template>

<style scoped>
.steps {
    text-align: center;
    margin-bottom: 60px;
}
.upload-form {
    width: 50%;
}
</style>
