from product import Product
from product import ProductManager
from user import User


class Seller(User):
    def __init__(self, product_manger: ProductManager):
        self.__product_manger = product_manger
        self.__products = []

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def add_product(self, name, price, category):
        self._product.price = price
        self._product.category = category
        self._product.product_name = name
        pr = Product(category, name, 0, 100)
        self.__product_manger.add_product(pr)
        self.__products.append(pr)

    def find_product(self, product_name):
        product: Product
        for product in self.__products:
            if product.get_product_name() == product_name:
                return product

    def increase_quantity(self, tmp, product_name):
        needed_product = self.find_product(product_name)
        needed_product.quantity += tmp

    def get_list_product(self):
        product: Product
        for product in self.__products:
            print(product.get_product_name(), end=" ")
            print(product.get_category(), end=" ")
            print(product.get_origin(), end=" ")
            print()
