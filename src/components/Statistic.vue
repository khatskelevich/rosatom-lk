<template>
    <div class="statistic">
        <el-row :gutter="16">
            <el-col :span="4">
                <div class="statistic-card">
                    <el-statistic :value="98">
                        <template #title>
                            <div style="display: inline-flex; align-items: center">
                                Выполнено (день)
                                <el-tooltip
                                        effect="dark"
                                        content="Количество готового продукта"
                                        placement="top"
                                >
                                    <el-icon style="margin-left: 4px" :size="12">
                                        <Warning/>
                                    </el-icon>
                                </el-tooltip>
                            </div>
                        </template>
                    </el-statistic>
                    <div class="statistic-footer">
                        <div class="footer-item">
                            <span>со вчера</span>
                            <span class="green">
              24%
              <el-icon>
                <CaretTop/>
              </el-icon>
            </span>
                        </div>
                    </div>
                </div>
            </el-col>
            <el-col :span="4">
                <div class="statistic-card">
                    <el-statistic :value="693">
                        <template #title>
                            <div style="display: inline-flex; align-items: center">
                                Выполнено (месяц)
                                <el-tooltip
                                        effect="dark"
                                        content="Количество готового продукта за месяц"
                                        placement="top"
                                >
                                    <el-icon style="margin-left: 4px" :size="12">
                                        <Warning/>
                                    </el-icon>
                                </el-tooltip>
                            </div>
                        </template>
                    </el-statistic>
                    <div class="statistic-footer">
                        <div class="footer-item">
                            <span>месяц к месяцу</span>
                            <span class="red">
              12%
              <el-icon>
                <CaretBottom/>
              </el-icon>
            </span>
                        </div>
                    </div>
                </div>
            </el-col>
            <el-col :span="4">
                <div class="statistic-card">
                    <el-statistic :value="72" title="Запланировано операций сегодня">
                        <template #title>
                            <div style="display: inline-flex; align-items: center">
                                Запланировано сегодня
                            </div>
                        </template>
                    </el-statistic>
                    <div class="statistic-footer">
                        <div class="footer-item">
                            <span>чем вчера</span>
                            <span class="green">
              16%
              <el-icon>
                <CaretTop/>
              </el-icon>
            </span>
                        </div>
                        <div class="footer-item">
                            <el-icon :size="14">
                                <ArrowRight/>
                            </el-icon>
                        </div>
                    </div>
                </div>
            </el-col>
            <el-col :span="4"/>

            <el-col :span="8">
                <el-text class="mx-1" size="large" align="left">
                    <h5>Процент загрузки печей</h5>
                </el-text>
                <el-progress :percentage="50" :stroke-width="8"/>
                <el-progress :percentage="100" :stroke-width="8"/>
                <el-progress :percentage="100" :stroke-width="8" status="success"/>
                <el-progress :percentage="100" :stroke-width="8" status="success"/>
                <el-progress :percentage="100" :stroke-width="8" status="success"/>
                <el-progress :percentage="100" :stroke-width="8" status="warning"/>
                <el-progress :percentage="50" :stroke-width="8" status="exception" :indeterminate="true" />
            </el-col>
        </el-row>
    </div>
</template>

<script lang="ts" setup>
import {
    ArrowRight,
    CaretBottom,
    CaretTop,
    Warning,
} from '@element-plus/icons-vue'
</script>

<style scoped>
.statistic, .progress {
    width: 100%;
}


.el-statistic {
    --el-statistic-content-font-size: 28px;
}

.statistic-card {
    height: 100%;
    padding: 20px;
    border-radius: 4px;
    background-color: var(--el-bg-color-overlay);

    box-shadow: var(--el-box-shadow-lighter);
}

.statistic-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    font-size: 12px;
    color: var(--el-text-color-regular);
    margin-top: 16px;
}

.statistic-footer .footer-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.statistic-footer .footer-item span:last-child {
    display: inline-flex;
    align-items: center;
    margin-left: 4px;
}

.green {
    color: var(--el-color-success);
}

.red {
    color: var(--el-color-error);
}
</style>

