from product import product
from product import product_manager
class Seller:
  def init(self):
    self._product = product()
    self.product_manger = product_manager()
  def add_product(self,name,price, category):
    self._product.price = price
    self._product.category = category
    self._product.product_name = name 
    self.product_manger.
  def increase_quantity(self,tmp):
    self._product.quantity += tmp
  