#!usr/bin/python3
import pickle

from utils import exceptions
from utils import messages


class Cinema:
    movies_list = []
    salon_list = {}

    def __int__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.__balance = 0.0

    @classmethod
    def add_salon_list(cls, name: str, capacity: int):
        if cls.is_salon_exist(name):
            raise exceptions.SameSalonFound(messages.Message.REPEATED_SALON_NAME)
        if capacity <= 0:
            raise exceptions.ZeroCapacityError(messages.Message.CAPACITY)

        cls.salon_list[name] = capacity

    @classmethod
    def save(cls):
        with open("database/cinema.pickle", "wb") as f:
            pickle.dump(cls.salon_list, f)
            del cls.salon_list

    @classmethod
    def load(cls):
        with open("database/cinema.pickle", "rb") as f:
            data = pickle.load(f)
        return data

    @staticmethod
    def get_salon(name: str):
        """
        getting salon object from salon dictionary
        @param name: string
        @return: salon object
        """
        if not Cinema.is_salon_exist(name):
            raise exceptions.NoSalonFound(messages.Message.NO_SALON_FOUND)

        cinema_data = Cinema.load()
        return cinema_data[name]

    @staticmethod
    def is_salon_exist(name: str):
        """
        check for salon name in salon dictionary
        @param name: string
        @return: boolean
        """
        return name in Cinema.load()
