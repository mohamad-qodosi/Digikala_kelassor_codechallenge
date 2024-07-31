class Kharidar :

    def __init__(self , name , password ) -> None:
        self.name = name
        self.password = password


class Order :

    def __init__(self , kharidar : Kharidar) -> None:
        self.kharidar = kharidar
        self.products = []

    def add_product (self , product : Product) :
        self.products.append(product)

    def order_list (self) : 
        for product in self.products : 
            print(product.get_name(), end= " " )
            print(product.get_category() , end = " ")
            print(product.get_city(), end =" " )
            print()

    
    


     