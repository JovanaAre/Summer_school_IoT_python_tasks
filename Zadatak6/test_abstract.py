from python.Zadatak6.abstract import ListAdder
from python.Zadatak6.abstract import DictAdder


def test_list_add():
    listadder1 = ListAdder([5, 3, 4])
    listadder2 = ListAdder(["string"])
    listadder3 = ListAdder([5, 3, 4, "string"])
    assert (listadder1.add(listadder2)).lista == listadder3.lista


def test_dict_add():
    dictadder1 = DictAdder({'Dd': 5, 'Ee': 4, 'Ff': 15})
    dictadder2 = DictAdder({'Aa': 25, 'Bb': 10, 'Cc': 20})
    dictadder3 = DictAdder({'Dd': 5, 'Ee': 4, 'Ff': 15, 'Aa': 25, 'Bb': 10, 'Cc': 20})
    assert (dictadder1.add(dictadder2)).dictionary == dictadder3.dictionary
