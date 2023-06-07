from Artemiy_hw_21.base_class import Storage


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