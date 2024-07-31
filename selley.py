from product import Product
from product import ProductManager


class Seller:
    def __init__(self, product_manger: ProductManager, name, password):
        self.__product_manger = product_manger
        self.__products = []
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
