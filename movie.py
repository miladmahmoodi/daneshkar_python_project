import pickle
from datetime import datetime

from utils.exceptions import *
from utils.messages import Message


class Movie:
    movie_list = {}

    def __init__(self, cinema: str, title: str, genre: str, discount: float, age_limit: int,
                 price: float, date_time: datetime = None):
        """
        :param cinema: Cinema name
        :param title: Movie title
        :param genre: Movie genre
        :param discount: Discount percentage
        :param age_limit: Age limit
        :param is_live: Is the movie live
        :param price: Movie price
        :param sold: Number of sold tickets
        :param date_time: Movie date and time
        :param total_sales: Total sales
        """
        self.cinema = cinema
        self.title = title
        self.genre = genre
        self.discount = discount
        self.age_limit = age_limit
        self.date_time = date_time if date_time else datetime.now()
        self.is_live = self.is_live()
        self.price = price
        self.sold = 0
        self.total_sales = 0

    @classmethod
    def create(cls, cinema: str, title: str, genre: str, discount: float, age_limit: int,
               price: float, date_time: datetime = None) -> dict:
        new_movie = cls(cinema, title, genre, discount, age_limit, price, date_time)
        cls.movie_list[title] = new_movie
        return cls.movie_list

    @classmethod
    def reserve(cls, movie: 'Movie') -> None:
        """
        Reserves a movie
        :param movie: Movie object
        :return: None
        """
        if not movie.is_live:
            raise ShowDoesNotExist(Message.SHOW_DOES_NOT_EXIST_MESSAGE)

        if datetime.now().date() != movie.date_time.date() or datetime.now().time() != movie.date_time.time():
            raise ShowDoesNotExist(Message.SHOW_DOES_NOT_EXIST_MESSAGE)

        movie.sold += 1
        movie.total_sales += 1
        return save_to_json(movie)

    def is_live(self) -> bool:
        pass

    @classmethod
    def save(cls):
        with open("database/movie.pickle", "wb") as f:
            pickle.dump(cls.movie_list, f)
            del cls.movie_list

    @classmethod
    def load(cls):
        with open("database/movie.pickle", "rb") as f:
            loaded_movie_list = pickle.load(f)
        return loaded_movie_list
