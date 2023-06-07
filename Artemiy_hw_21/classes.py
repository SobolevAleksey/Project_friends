# Try
import logging
from abc import ABC, abstractmethod

class Storage(ABC):
    stores_lst = []
    stores_names = []
    shops_lst = []
    shops_names = []

    def __init__(self, capacity: int, name: str):
        self._items = {}
        self._capacity = capacity
        self.name = name

    @abstractmethod
    def add(self, title: str, quantity: int):
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

class Store(Storage):

    def __init__(self, name):
        super().__init__(capacity=100, name=name)
        self._items = {}
        Storage.stores_lst.append(self)
        Storage.stores_names.append(self.name)

    def add(self, title: str, quantity: int):
        self._items[title] = self._items.get(title, 0) + quantity

    def remove(self, title: str, quantity: int):
        if title not in self._items:
            print("Такого товара на складе нет ")
            return False

        elif quantity > self._items.get(title):
            print("Нет необходимого количества товара на складе")
            return False

        self._items[title] = self._items.get(title) - quantity

    def get_free_space(self):
        free_space = self._capacity - self.get_unique_items_count()
        return free_space

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        total_quantity = sum(list(self.get_items().values()))
        return total_quantity

class Shop(Storage):
    def __init__(self, name):
        super().__init__(capacity=20, name=name)
        self._items = {}
        Storage.shops_lst.append(self)
        Storage.shops_names.append(self.name)

    def add(self, title: str, quantity: int):
        if self.get_free_space() < quantity:
            print("В магазине нет свободного места")
            return False
        elif len(self.get_items()) == 5 and title not in self._items:
            print("В магазине хранится максимальное количество наименований")
            return False
        self._items[title] = self._items.get(title, 0) + quantity

    def remove(self, title: str, quantity: int):
        if title not in self._items:
            print("Такого товара в магазине нет")
            return False
        elif self._items[title] < quantity:
            print("Нет необходимого количества товара. Вы можете заказать на скаде")
            return False
        self._items[title] = self._items.get(title) - quantity

    def get_free_space(self):
        free_space = self._capacity - self.get_unique_items_count()
        return free_space

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        total_quantity = sum(list(self.get_items().values()))
        return total_quantity



class Request():
    def __init__(self, sentence):
        info_lst = self.get_info_objs(sentence)
        if info_lst[4] not in Storage.stores_names:
            print("Такого склада не существует")
            pass
        self.fr = info_lst[4]
        if info_lst[6] not in Storage.shops_names:
            print("Такого магазина не существует")
            pass
        self.to = info_lst[6]
        self.amount = int(info_lst[1])
        self.product = info_lst[2]
        self.__repr__()



    def get_info_objs(self, sentence: str):
        info = sentence.split(" ")
        return info



    def __repr__(self):
        return f"Доставить {self.amount} {self.product} со склада {self.fr} в магазин {self.to}"


REQ_FORM = "Доставить 3 перец со_склада store_1 в_магазин shop_1"

