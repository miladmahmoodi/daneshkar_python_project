import pickle
from datetime import datetime
from cinema import Cinema
from utils.exceptions import *
from utils.messages import Message
from user import User
from bank import Bank


class Movie:
    movie_list = {}

    def __init__(self, cinema: str, salon: str, title: str, genre: str, discount: float, age_limit: int,
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
        self.salon = salon
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

    # def reserve(self, cinema: "Cinema", user: "User", bank: "Bank") -> None:
    #     """
    #
    #     @param cinema:
    #     @param user:
    #     @return:
    #     """
    #
    #     if not self.is_live:
    #         raise ShowDoesNotExist(Message.SHOW_DOES_NOT_EXIST_MESSAGE)
    #
    #     if self.age_limit <= user.age:
    #         raise AgeLimit(Message.AGE_LIMIT_ERROR)
    #
    #     bank.
    #     user.movies_list.append(self)
    #     salon_data = cinema.get_salon(self.salon)
    #     salon_data["capacity"] -= 1

    def is_live(self) -> bool:
        if self.date_time <= datetime.now():
            return True

        return False

    @classmethod
    def save(cls):
        with open("database/movie.pickle", "wb") as f:
            pickle.dump(cls.movie_list, f)
        cls.movie_list.clear()

    @classmethod
    def load(cls):
        with open("database/movie.pickle", "rb") as f:
            loaded_movie_list = pickle.load(f)
        return loaded_movie_list

    def final_price(self, user: "User"):
        final_price = self.price
        if user.birthday.day == self.date_time.day and user.birthday.month == user.birthday.month:
            final_price -= type(self).apply_discount(self.price, 0.5)

        time_passed = datetime.now() - self.date_time
        month_passed = int(time_passed.days / 30)
        if month_passed > 100:
            month_passed = 100

        final_price -= type(self).apply_discount(self.price, month_passed)
        return final_price

    @staticmethod
    def apply_discount(price: float, discount: float = 0.0) -> float:
        """

        @param price:
        @param discount:
        @return:
        """
        if not 0 <= discount <= 1:
            raise DiscountError(Message.DISCOUNT_ERROR)

        discount_price = price * discount
        return discount_price
