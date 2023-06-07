from Artemiy_hw_21.base_class import Storage


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
