# Росатом ЛК Диспетчера [Кади]

<img src="./public/rosatomlogo.png">

[![GitHub last commit](https://img.shields.io/github/last-commit/khatskelevich/rosatom-lk)](https://github.com/khatskelevich/rosatom-lk/commits/main)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/khatskelevich/rosatom-lk)](https://github.com/khatskelevich/rosatom-lk)
![GitHub top language](https://img.shields.io/github/languages/top/khatskelevich/rosatom-lk)
![Node](https://img.shields.io/badge/node-%3E%3D18.0.0-brightgreen)
![Yarn](https://img.shields.io/badge/yarn-%3E%3D1.22.0-blue)
![Python](https://img.shields.io/badge/python-3.9-blue)
![Dependencies](https://img.shields.io/badge/dependencies-matplotlib%2C%20pandas%2C%20numpy%2C%20catboost%2C%20deap%2C%20scipy%2C%20sklearn-yellow)

## О проекте

Росатом ЛК Диспетчера - это комплексное решение, объединяющее UI интерфейс, обработчик данных и нейронную сеть для эффективного планирования загрузки печей на предприятии.

### Ветки проекта

- **main**: UI интерфейс, написанный на Electron & VueJS
- **handler**: Обработчик данных, обрабатывающий входные данные через нейронную сеть и возвращающий их на фронт
- **ai**: Нейронная сеть и модель, используемые для анализа данных

## Использование

#### - Открыть директорию `/out`
#### - Запустить файл `rosatom.exe`

### Для AI
#### - Определить файл .json для данных
#### - Запустить `python3 ai_main.py`

## Разработка

#### Для UI
```shell
yarn 
```
#### Для Обработчика
```shell
pip install matplotlib pandas numpy catboost deap scipy scikit-learn
```


#### Для локальной разработки:
```shell
yarn start
```

#### Для сборки приложение:
```shell
yarn build
yarn make
```
