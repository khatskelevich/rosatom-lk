import json
from datetime import datetime

class Process:
    def __init__(self, name, data):
        self.name = name
        self.data = self._convert_time(data)

    def _convert_time(self, data):
        for item in data:
            if isinstance(item['y'], str):
                dt = datetime.strptime(item['y'], "%Y-%m-%dT%H:%M:%S.%fZ")
                item['y'] = int(dt.timestamp())
        return data

    def change_name(self, new_name):
        self.name = new_name

    def change_time(self, oven, new_time):
        new_time = self._convert_time([{'x': '', 'y': new_time}])[0]['y']
        for item in self.data:
            if item['x'] == oven:
                item['y'] = new_time

    def change_oven_name(self, old_name, new_name):
        for item in self.data:
            if item['x'] == old_name:
                item['x'] = new_name

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

p = Process('Отжиг', [{'x': 'Печь 1', 'y': '2009-09-01T00:00:00.000Z'}])
print(p.to_json())
p.change_name('Нагрев')
p.change_time('Печь 1', '2009-09-02T00:00:00.000Z')
p.change_oven_name('Печь 1', 'Печь 2')
print(p.to_json())
