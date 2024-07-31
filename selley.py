from product import Product
from product import ProductManager


class Seller:
    def init(self, name, password):
        self.product_manger = ProductManager()
        self.name = name
        self.password = password

    def add_product(self, name, price, category):
        self._product.price = price
        self._product.category = category
        self._product.product_name = name
        self.product_manger.product_list.append(self)

    def increase_quantity(self, tmp):
        self._product.quantity += tmp
