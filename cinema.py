#!usr/bin/python3

from utils import exceptions
from utils import messages


class Cinema:
    movies_list = []
    salon_list = {}

    def __int__(self, name: str, location: str, balance: float):
        self.name = name
        self.location = location
        self.__balance = balance

    @classmethod
    def add_salon_list(cls, name: str, capacity: int):
        if not Cinema.is_salon_exist(name):
            if capacity > 0:
                cls.salon_list[name] = capacity
            else:
                raise exceptions.ZeroCapacityError(messages.Message.CAPACITY)
        else:
            raise exceptions.SameSalonFound(messages.Message.REPEATED_SALON_NAME)

    def save(self):
        pass

    @staticmethod
    def get_salon(name: str):
        if not Cinema.is_salon_exist(name):
            raise exceptions.NoSalonFound(messages.Message.NO_SALON_FOUND)
        else:
            return Cinema.salon_list[name]

    @staticmethod
    def is_salon_exist(name: str):
        return name in Cinema.salon_list
