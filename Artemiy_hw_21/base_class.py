from abc import abstractmethod, ABC


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