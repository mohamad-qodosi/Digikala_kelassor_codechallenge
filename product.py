class Product:
    def __init__(self, category, product_name, procceing_time, quantiy, price) -> None:
        self.__category = category
        self.__product_name = product_name
        self.__procceing_time = procceing_time
        self.__quantity = quantiy
        self.__price = price
        self.__origin = None

    def set_origin(self, origin):
        self.origin = origin


class ProductManager:
    def __init__(self) -> None:
        self.product_list = []

    def search_product(self, product_name):
        for product in self.product_list:
            if product.__product_name == product_name:
                return product
        return False

    def search_category(self, category):
        reserve = []
        for product in self.product_list:
            if product.__category == category:
                reserve.append(product)
        return reserve

    def search_by_price(self, price_range):
        show = []
        for product in self.product_list:
            if price_range[0] < product.__price < price_range[1]:
                show.append(product)
        return show

    def add_product(self, product_obj):
        self.product_list.append(product_obj)
