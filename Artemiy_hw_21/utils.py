from classes import Storage, Request


def search_store(name):
    for store in Storage.stores_lst:
        if name == store.name:
            return store


def search_shop(name):
    for shop in Storage.shops_lst:
        if name == shop.name:
            return shop