from product import Product
from product import ProductManager


class Seller:
    def init(self, name, password):
        self.__product_manger = ProductManager()
        self.__name = name
        self.__password = password

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def seller_product_managet(self):
        return self.__product_manger

    def add_product(self, name, price, category):
        self._product.price = price
        self._product.category = category
        self._product.product_name = name
        self.__product_manger.product_list.append(self)

    def increase_quantity(self, tmp):
        self._product.quantity += tmp
