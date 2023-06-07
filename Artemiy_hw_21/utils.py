from request_class import Storage


def search_store(storage_name):
    """Функция для опеределения, что товар доставляется в магазин"""
    for store in Storage.stores_lst:
        if storage_name == store.name:
            return store


def search_shop(storage_name):
    """Функция для опеределения, что товар доставляется в хранилище"""
    for shop in Storage.shops_lst:
        if storage_name == shop.name:
            return shop