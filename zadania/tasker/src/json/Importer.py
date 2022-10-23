import json
import sys


class Importer:

    def __init__(self):
        self.data = []
        #tu się powinno użyć pewnie relative path ale nie umiem :////
        #no bo nie wiem jest inny folder i nie da się użyć "."
        self.path = 'C://path//to/task//tasker//taski.json'

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        self.data = json.load(open(self.path,'r', encoding = 'utf8'))

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.data

