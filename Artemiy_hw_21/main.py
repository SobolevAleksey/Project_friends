from Artemiy_hw_21.shop_class import Shop
from Artemiy_hw_21.store_class import Store
from request_class import Request
from utils import search_shop, search_store

store_1 = Store("store_1")
shop_1 = Shop("Shop_1")
store_2 = Store("store_2")
shop_2 = Shop("Shop_2")


def add_data():
    "Добавляем товары на склады"
    store_1.add("морковь", 20)
    store_1.add("лук", 20)
    store_1.add("перец", 20)
    store_1.add("виноград", 20)
    store_1.add("арбуз", 20)
    store_1.add("картофель", 0)

    shop_1.add("морковь", 0)
    shop_1.add("картофель", 0)
    shop_1.add("лук", 4)
    shop_1.add("перец", 4)
    shop_1.add("арбуз", 4)

    store_2.add("морковь", 20)
    store_2.add("лук", 20)
    store_2.add("перец", 0)
    store_2.add("виноград", 20)
    store_2.add("арбуз", 20)
    store_2.add("манго", 20)

    shop_2.add("морковь", 4)
    shop_2.add("картофель", 4)
    shop_2.add("лук", 4)
    shop_2.add("перец", 0)


def main():
    print(
        "\n\nДобро пожаловать в интернет-магазин 'Овощной Микс'! \n\nВыберите одно из наших отделений, чтобы сделать онлайн-покупку")

    print(f"\n{shop_1.name} В наличии есть следующие товары: {shop_1.get_items()}")
    print(f"\n{shop_2.name} В наличии есть следующие товары: {shop_2.get_items()} \n")

    print("Если хотите сделать покупку в магазине Shop_1, нажмите 1;\nв магазине Shop_2 - нажмите 2")
    shop_el = int(input("\nНомер отделения: "))
    while True:
        if shop_el == 1:
            shop = shop_1
            break
        elif shop_el == 2:
            shop = shop_2
            break
        else:
            print("Такого отделения не существует")
            exit()

    print(f"Добро пожаловать в {shop.name}!")
    while True:

        user_input = input(
            "Нажмите Enter для составления заказа. Чтобы закончить или перейти в меню склада, введите 0\n")

        if user_input == "0":
            break
        try:
            sh_goods_title = input("Напишите точное наименование товара: ").lower()
            sh_goods_quantity = int(input("Напишите точное количество товара: "))
        except ValueError:
            print("Введите правильные значения: Наименование - буквами,  Количество - цифрой")
            continue
        if shop.remove(sh_goods_title, sh_goods_quantity) == False:
            continue
        else:
            print(f"\nКурьер забрал из магазина {sh_goods_quantity} {sh_goods_title} и направляется по вашему адресу")

        print("\nАктуальный каталог магазина", shop.get_items())

    print(f"СКЛАД: заполните форму и наш курьер доставит товар в один из магазинов")

    while True:
        user_input = input("Нажмите Enter для составления заказа. Чтобы закончить, введите 0\n")
        if user_input == "0":
            break
        print(f"\nДоступные склады: {shop.stores_names}\nДоступные магазины: {shop.shops_names}\n")
        print("Заполните следующую форму, заменив слова в  скобках на данные без скобок")
        print(
            "Доставить (количество цифрой) (товар в им. падеже) со_склада (название склада) в_магазин (название магазина)")

        sentence = input("Напишите заказ:\n")

        try:
            req = Request(sentence)

        except IndexError:
            print("Неправильно заполнена форма заказа")
            continue

        store = search_store(req.fr)
        shop = search_shop(req.to)

        if store.remove(req.product, req.amount) == False:
            continue

        if shop.add(req.product, req.amount) == False:
            continue

        print(f"Курьер забрал {req.amount} {req.product} со склада {req.fr}")
        print(f"Курьер везет {req.amount} {req.product} со склада {req.fr} в магазин {req.to}")
        print(f"Курьер доставил {req.amount} {req.product} в магазин {req.to}")

        print(f"Текущий каталог склада {req.fr}:\n {store.get_items()}")
        print("\nАктуальный каталог магазина", shop.get_items())


if __name__ == '__main__':
    add_data()
    main()
