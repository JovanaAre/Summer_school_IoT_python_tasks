# 6. Napisati abstraktnu klasu Adder koja definise metodu add(self,x,y).
# Zatim napisati dve klase koje nasledjuju abstraktnu klasu Adder
# i imeplementiraju add() metodu. Te dve klase su:
# ListAdder - cija metoda add() vraća kao rezultat konkatenaciju dve liste.
# DictAdder - čija metoda add() vraća kao rezultat novi rečnik
# koji sadrži sve elemente iz dva prosledjena rečnika


from python.Zadatak6.abstract_exp import BadArgumentException
from abc import ABCMeta, abstractmethod


class Adder:
    """
    Abstract class used for abstract implementation of the method add.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, other):
        """
        Abstract method used for adding given object to other object
        :param other: Other object to be added
        :return: The object representing the sum of the self and other
        """
        pass


class ListAdder(Adder):
    """
    A class inherited from class Adder used to override the add method
    that concatenates two lists

    Methods
    -------
    __init__(lista: list = None):
    Constructs the necessary attribute for the ListAdder object.
    :param lista: list object
    """
    def __init__(self, lista: list = None):
        self._lista_ = []
        if lista is not None and isinstance(lista, list):
            self._lista_ = lista

    @property
    def lista(self):
        return self._lista_

    def add(self, other):
        if other is not None and isinstance(other, ListAdder):
            new_lista = self.lista + other.lista
            return ListAdder(new_lista)
        raise BadArgumentException("Provided argument is not an instance of the ListAdder")


class DictAdder(Adder):
    """
    A class inherited from class Adder used to override the add method
    to concatenates two dictionaries

    Methods
    -------
    __init__(dictionary: dict = None):
    Constructs the necessary attribute for the DictAdder object.
    :param dictionary: dict object
    """

    def __init__(self, dictionary: dict = None):
        self._dictionary_ = {}
        if dictionary is not None and isinstance(dictionary, dict):
            self._dictionary_ = dictionary

    @property
    def dictionary(self):
        return self._dictionary_

    def add(self, other):
        if other is not None and isinstance(other, DictAdder):
            new_dictionary = {}
            new_dictionary.update(self.dictionary)
            new_dictionary.update(other.dictionary)
            return DictAdder(new_dictionary)
        raise BadArgumentException("Provided argument is not an instance of the DictAdder")


# print(Adder.__doc__)
# print(ListAdder.__doc__)
# print(DictAdder.__doc__)
