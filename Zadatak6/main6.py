from python.Zadatak6.abstract import ListAdder
from python.Zadatak6.abstract import DictAdder

listadder1 = ListAdder([1, 2, 3])
listadder2 = ListAdder(["string", 5, 6])
listadder3 = listadder1.add(listadder2)
print("Nakon konkatenacije lista dobija se lista: ")
print(listadder3.lista)

dictadder1 = DictAdder({'rtrk': 5, 'python': 4, 'course': 15})
dictadder2 = DictAdder({'A': 25, 'B': 10, 'C': 20})
dictadder3 = dictadder1.add(dictadder2)
print("Nakon konkatenacije rjecnika dobija se rjecnik: ")
print(dictadder3.dictionary)
