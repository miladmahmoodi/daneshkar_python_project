from utils.exceptions import *
from utils.messages import Message


class Movie:
    def __init__(self, cinema: str, title: str, genre: str, discount: float, age_limit: int, date_time: dict,
                 is_live: bool, price: float, sold: float):
        """
        A class used to represent Movie.

        :param cinema: A string representing the cinema of the movie.
        :param title: A string representing the title of the movie.
        :param genre: A string representing the genre of the movie.
        :param discount: A float representing the discount of the movie.
        :param age_limit: An integer representing the age limit of the movie.
        :param date_time: A dictionary representing the date and time of the movie.
        :param is_live: A boolean representing the status of the movie.
        :param price: A float representing the price of the movie.
        :param sold: A float representing the sold of the movie.
        """
        self.cinema = cinema
        self.title = title
        self.genre = genre
        self.discount = discount
        self.age_limit = age_limit
        self.date_time = date_time
        self.is_live = is_live
        self.price = price
        self.sold = sold

    @classmethod
    def create(cls, cinema: str, title: str, genre: str, discount: float, age_limit: int, date_time: dict,
               is_live: bool, price: float, sold: float) -> 'Movie':
        """
        Create a new instance of Movie.

        :param cinema: A string representing the cinema of the movie.
        :param title: A string representing the title of the movie.
        :param genre: A string representing the genre of the movie.
        :param discount: A float representing the discount of the movie.
        :param age_limit: An integer representing the age limit of the movie.
        :param date_time: A dictionary representing the date and time of the movie.
        :param is_live: A boolean representing the status of the movie.
        :param price: A float representing the price of the movie.
        :param sold: A float representing the sold of the movie.
        """
        return cls(cinema, title, genre, discount, age_limit, date_time, is_live, price, sold)

    def reserve(self, user_age: int, current_date_time: dict) -> bool:
        """
        Reserve the movie for the user.

        :param user_age: An integer representing the age of the user.
        :param current_date_time: A dictionary representing the current date and time.
        """
        if not self.is_live:
            raise ShowDoesNotExist(Message.SHOW_DOES_NOT_EXIST_MESSAGE)

        if user_age < self.age_limit:
            raise AgeLimitError(Message.AGE_LIMIT_ERROR_MESSAGE)

        if current_date_time["date"] != self.date_time["date"] or current_date_time["time"] != self.date_time["time"]:
            raise ShowDoesNotExist(Message.SHOW_DOES_NOT_EXIST_MESSAGE)

        self.sold += 1
        print(f"Reservation successful for {self.title} at {self.cinema}.")
        return True
