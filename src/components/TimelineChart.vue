<script setup>
import {onMounted} from 'vue'
import ApexCharts from 'apexcharts'
import ru from 'apexcharts/dist/locales/ru.json'


const options = {
    series: [
        {
            name: 'Отжиг',
            data: [
                {
                    x: 'Печь 1',
                    y: [
                        new Date(2023, 3, 30, 12, 30).getTime(),
                        new Date(2023, 3, 30, 13).getTime()
                    ]
                },
            ]
        },
        {
            name: 'Нагрев',
            data: [
                {
                    x: 'Печь 1',
                    y: [
                        new Date(2023, 3, 30, 10).getTime(),
                        new Date(2023, 3, 30, 12).getTime()
                    ]
                },
                {
                    x: 'Печь 2',
                    y: [
                        new Date(2023, 3, 30, 12).getTime(),
                        new Date(2023, 3, 30, 14).getTime()
                    ]
                },
                {
                    x: 'Печь 3',
                    y: [
                        new Date(2023, 3, 30, 9).getTime(),
                        new Date(2023, 3, 30, 11).getTime()
                    ]
                },
                {
                    x: 'Печь 5',
                    y: [
                        new Date(2023, 3, 30, 10).getTime(),
                        new Date(2023, 3, 30, 12).getTime()
                    ]
                }
            ]
        },
        {
            name: 'Подогрев',
            data: [
                {
                    x: 'Печь 2',
                    y: [
                        new Date(2023, 3, 30, 14, 20).getTime(),
                        new Date(2023, 3, 30, 14, 30).getTime()
                    ]
                },
                {
                    x: 'Печь 4',
                    y: [
                        new Date(2023, 3, 30, 12).getTime(),
                        new Date(2023, 3, 30, 14).getTime()
                    ]
                },
                {
                    x: 'Печь 5',
                    y: [
                        new Date(2023, 3, 30, 12).getTime(),
                        new Date(2023, 3, 30, 14).getTime()
                    ]
                }
            ]
        },
        {
            name: 'Ковка',
            data: [
                {
                    x: 'Печь 1',
                    y: [
                        new Date(2023, 3, 30, 12).getTime(),
                        new Date(2023, 3, 30, 12, 30).getTime()
                    ]
                }
            ]
        },
        {
            name: 'Прокат',
            data: [
                {
                    x: 'Печь 2',
                    y: [
                        new Date(2023, 3, 30, 14).getTime(),
                        new Date(2023, 3, 30, 14, 20).getTime()
                    ]
                }, {
                    x: 'Печь 2',
                    y: [
                        new Date(2023, 3, 30, 14, 30).getTime(),
                        new Date(2023, 3, 30, 14, 50).getTime()
                    ]
                }, {
                    x: 'Печь 4',
                    y: [
                        new Date(2023, 3, 30, 13).getTime(),
                        new Date(2023, 3, 30, 14).getTime()
                    ]
                }
            ]
        },
        {
            name: "Рэмонт",
            data: [{
                x: 'Печь 6',
                y: [
                    new Date(2023, 3, 30, 14, 30).getTime(),
                    new Date(2023, 3, 30, 16, 30).getTime(),
                    // new Date(2023, 4, 30, 14, 50).getTime()
                ]
            }, {
                x: 'Печь 7',
                y: [
                    new Date(2023, 3, 30, 13).getTime(),
                    new Date(2023, 3, 30, 16).getTime(),
                    //new Date(2023, 4, 30, 14).getTime()
                ]
            }]
        }
    ],
    chart: {
        locales: [ru],
        defaultLocale: 'ru',
        height: 350,
        type: 'rangeBar' // подумать о смене на bar
    },
    plotOptions: {
        bar: {
            horizontal: true,
            barHeight: '30%',
            rangeBarGroupRows: true
        }
    },
    colors: [
        "#d74126","#F86624", "#FEB019",
        "#8D5B4C", "#546E7A", "#5d5d5d"
    ],
    fill: {
        type: 'solid'
    },
    xaxis: {
        type: 'datetime',
        categories: [
            "Печь 1",
            "Печь 2",
            "Печь 3",
            "Печь 4",
            "Печь 5",
            "Печь 6",
            "Печь 7"
        ]
    },
    legend: {
        position: 'bottom'
    },
    // tooltip: {
    //     custom: function (opts) {
    //         const fromYear = new Date(opts.y1).getFullYear()
    //         const toYear = new Date(opts.y2).getFullYear()
    //         const values = opts.ctx.rangeBar.getTooltipValues(opts)
    //
    //         return (
    //             ''
    //         )
    //     }
    // }
};

onMounted(() => {
    const chart = new ApexCharts(document.querySelector("#timeline"), options);
    chart.render();
})
</script>

<template>
    <div id="timeline"/>
</template>

<style scoped>

</style>
