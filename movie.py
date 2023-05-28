import json
from datetime import datetime

from utils.exceptions import *
from utils.messages import Message


def save_to_json(movie: 'Movie'):
    movie_data = {
        "cinema": movie.cinema,
        "title": movie.title,
        "genre": movie.genre,
        "discount": movie.discount,
        "age_limit": movie.age_limit,
        "date_time": movie.date_time.isoformat(),
        "is_live": movie.is_live,
        "price": movie.price,
        "sold": movie.sold,
        "total_sales": movie.total_sales
    }

    with open('database/movies.json', "w") as json_file:
        json.dump(movie_data, json_file)


class Movie:
    def __init__(self, cinema: str, title: str, genre: str, discount: float, age_limit: int,
                 is_live: bool, price: float, sold: float, date_time: datetime = None, total_sales: int = 0):
        self.cinema = cinema
        self.title = title
        self.genre = genre
        self.discount = discount
        self.age_limit = age_limit
        self.date_time = date_time if date_time else datetime.now()
        self.is_live = is_live
        self.price = price
        self.sold = sold
        self.total_sales = total_sales

    @classmethod
    def create(cls, cinema: str, title: str, genre: str, discount: float, age_limit: int,
               is_live: bool, price: float, sold: float) -> None:
        return save_to_json(cls(cinema, title, genre, discount, age_limit, is_live, price, sold))

    @classmethod
    def reserve(cls, movie: 'Movie') -> None:
        if not movie.is_live:
            raise ShowDoesNotExist(Message.SHOW_DOES_NOT_EXIST_MESSAGE)

        if datetime.now().date() != movie.date_time.date() or datetime.now().time() != movie.date_time.time():
            raise ShowDoesNotExist(Message.SHOW_DOES_NOT_EXIST_MESSAGE)

        movie.sold += 1
        movie.total_sales += 1
        return save_to_json(movie)
