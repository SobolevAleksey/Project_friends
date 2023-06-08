from Artemiy_hw_21.base_class import Storage


class Request():
    def __init__(self, sentence):
        info_lst = sentence.split(" ")

        if info_lst[5] not in Storage.stores_names:
            print("Такого склада не существует")

        self.fr = info_lst[4]

        if info_lst[8] not in Storage.shops_names:
            print("Такого магазина не существует")

        self.to = info_lst[8]
        self.amount = int(info_lst[1])
        self.product = info_lst[2]
        self.__repr__()

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} со склада {self.fr} в магазин {self.to}"


REQ_FORM = "Доставить 3 перец со склада store_1 в магазин shop_1"
