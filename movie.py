import pickle
from datetime import datetime
from cinema import Cinema
from utils.exceptions import *
from utils.messages import Message
from user import User
from bank import Bank
from utils.user_utils import Utils


class Movie:
    movie_list = {}

    def __init__(
            self,
            cinema: 'Cinema',
            title: str,
            genre: str,
            age_limit: int,
            price: float,
            date_time: str,
            discount: float = 0.0,
    ) -> None:
        """

        :param cinema:
        :param title:
        :param genre:
        :param age_limit:
        :param price:
        :param date_time:
        :param discount:
        """
        self.cinema = cinema
        self.title = title
        self.genre = genre
        self.age_limit = age_limit
        self.price = price
        self.date_time = Utils.check_date(date_time)
        self.discount = discount
        self.is_live = self.is_live()
        self.sold = 0
        self.total_sales = 0

        type(self).movie_list[title] = self

    @classmethod
    def create(
            cls,
            cinema: 'Cinema',
            title: str,
            genre: str,
            age_limit: int,
            price: float,
            date_time: str,
            discount: float,
    ) -> None:

        cls(
            cinema,
            title,
            genre,
            age_limit,
            price,
            date_time,
            discount,
        ).save()

    def can_reserve(self, count: int, user: 'User') -> bool:
        """

        :param count:
        :param user:
        :return:
        """

        salon_data = Cinema.get_salon()

        if not user.get_age > self.age_limit:
            raise AgeLimitError(Message.AGE_LIMIT_ERROR)
        if not self.is_live:
            raise ShowDoesNotExist(Message.SHOW_DOES_NOT_EXIST_MESSAGE)
        if Cinema. < count:
            raise SalonFullCapacity(Message.SALON_FULL_CAPACITY)

        return True

    def reserve(self, cinema: "Cinema", user: "User") -> None:
        """

        @param cinema:
        @param user:
        @return:
        """

        if not self.is_live:
            raise ShowDoesNotExist(Message.SHOW_DOES_NOT_EXIST_MESSAGE)

        if self.age_limit <= user.get_age:
            raise AgeLimit(Message.AGE_LIMIT_ERROR)

        user.movies_list.append(self)
        salon_data = cinema.get_salon(self.salon)
        salon_data["capacity"] -= 1

    def is_live(self) -> bool:
        if self.date_time <= datetime.now():
            return True

        return False

    @classmethod
    def save(cls):
        with open("../database/movie.pickle", "ab") as f:
            pickle.dump(cls.movie_list, f)
        cls.movie_list.clear()

    @classmethod
    def load(cls):
        try:
            with open("../database/movie.pickle", "rb") as f:
                loaded_movie_list = pickle.load(f)
        except EOFError as err:
            return dict()
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
