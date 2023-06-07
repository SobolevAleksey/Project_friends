from Artemiy_hw_21.base_class import Storage


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
