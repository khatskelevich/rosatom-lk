# Neural Network Handler

![Python](https://img.shields.io/badge/python-3.9-blue)
![Dependencies](https://img.shields.io/badge/dependencies-numpy%2C%20matplotlib-yellow)

Этот скрипт представляет собой обработчик данных для нейронной сети. Он принимает входные данные, запускает нейронную сеть и возвращает результат.

## Использование

```bash
pip install -r requirements.txt
```

```bash
python handler.py --input <входные_данные> [--save_results] [--console_output] [--generate_plots]
```

### Флаги

    --input (обязательный): Путь к входным данным для нейронной сети.
    --save_results: Сохранить результаты в файл.
    --console_output: Вывести результаты в консоль.
    --generate_plots: Сгенерировать графики результатов.

### Пример использования класса Process

```python
import process

# Создание процесса
p = process.Process('Отжиг', [{'x': 'Печь 1', 'y': '2009-09-01T00:00:00.000Z'}])
print(p.to_json())

# Изменение имени и времени
p.change_name('Нагрев')
p.change_time('Печь 1', '2009-09-02T00:00:00.000Z')

# Изменение имени печи
p.change_oven_name('Печь 1', 'Печь 2')
print(p.to_json())
```