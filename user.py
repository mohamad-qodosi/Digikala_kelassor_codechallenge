from product import Product
from selley import Seller
from kharidar_order import Kharidar
from kharidar_order import Order


class UserManager:
    def __init__(self) -> None:
        self.users = []

    def add_user(self, name, password):
        self.users.append(User(name, password))

    def validation(self, name, password, role):
        user: User
        flag = 0
        for user in self.users:
            if user.get_name() == name and user.get_password() == password:
                return user
        if flag == 0:
            return False


class User:
    def __init__(self, name, password, role) -> None:
        self.name = name
        self.password = password
        self.role = role

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password
