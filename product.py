class product:
    def __init__(self , category , product_name,  procceing_time, quantiy , price) -> None:
        self.category = category
        self.product_name = product_name
        self.procceing_time = procceing_time
        self.quantity = quantiy
        self.price = price
        self.origin = None
    
    def set_origin(self,origin):
        self.origin = origin

class product_manager:
    def __init__(self) -> None:
        self.product_list = []

    def search_product(self ,product_name):
        pass

    def search_category(self , category):
        pass

    def search_by_price(self , price_range):
        pass

    def add_product(self , product_obj):
        pass