import json


class Exporter:

    def __init__(self):
        self.new_data = []
        self.path = 'C://path//to//task//tasker//taski.json'

    def save_tasks(self, tasks):
        #self.new_data = json.load(open(self.path,'a', encoding = 'utf8'))
        #new_data = json.dump(tasks,indent =2)
        with open(self.path,'w', encoding='utf8') as f:
            json.dump(tasks, f, indent = 2, ensure_ascii=False)
