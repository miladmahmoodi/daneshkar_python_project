#!usr/bin/python3
import pickle

from utils import exceptions
from utils import messages


class Cinema:
    movies_list = []
    salon_list = {}
    cinema_list = {}

    def __int__(self, name: str, location: str, salon_count: int):
        self.name = name
        self.location = location
        self.salon_count = salon_count
        self.__balance = 0.0

        type(self).cinema_list[name] = self

    @classmethod
    def create(cls, name: str, location: str, salon_count: int) -> "Cinema":
        """

        @param name:
        @param location:
        @param salon_count:
        @return:
        """

        cinema = cls(name, location, salon_count)
        return cinema

    def add_salon_list(self, name: str, capacity: int):
        if self.is_salon_exist(name):
            raise exceptions.SameSalonFound(messages.Message.REPEATED_SALON_NAME)
        if capacity <= 0:
            raise exceptions.ZeroCapacityError(messages.Message.CAPACITY)

        type(self).salon_list[name] = {"capacity": capacity, "is_accessible": True}
        type(self).save("salon")

    @classmethod
    def save(cls, name: str, obj: "Cinema" = None) -> None:
        match name:
            case "cinema":
                with open("database/cinema.pickle", "wb") as f:
                    pickle.dump(cls.cinema_list, f)
                    cls.cinema_list.clear()
            case "salon":
                with open("database/salon.pickle", "wb") as f:
                    cinema_salon = dict()
                    cinema_salon[obj.name] = cls.salon_list
                    pickle.dump(cinema_salon, f)
                    cls.cinema_list.clear()
                    cinema_salon.clear()

    @classmethod
    def load(cls, name: str) -> dict:
        match name:
            case "cinema":
                with open("database/cinema.pickle", "rb") as f:
                    data = pickle.load(f)
            case "salon":
                with open("database/salon.pickle", "rb") as f:
                    data = pickle.load(f)

        return data

    def get_salon(self, name: str):
        """
        getting salon object from salon dictionary
        @param name: string
        @return: salon object
        """
        if not self.is_salon_exist(name):
            raise exceptions.NoSalonFound(messages.Message.NO_SALON_FOUND)

        cinema_data = Cinema.load("salon")
        salon_data = cinema_data[self.name]
        return salon_data

    def is_salon_exist(self, name: str):
        """
        check for salon name in salon dictionary
        @param name: string
        @return: boolean
        """
        cinema_data = type(self).load("salon")
        salon_data = cinema_data[self.name]
        return name in salon_data

