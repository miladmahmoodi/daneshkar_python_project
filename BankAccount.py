#! usr/bin/python3

from abc import ABC, abstractmethod
from utils import exceptions
from utils.messages import Message


class BankAccount(ABC):
    MINIMUM_BALANCE = 10_000

    def __init__(self, owner_name: str, cvv2: str, password: str, balance: float) -> None:
        """

        :param owner_name:
        :param cvv2:
        :param password:
        :param balance:
        """

        self.owner_name = owner_name
        self._balance = balance
        self.__password = password
        self.cvv2 = cvv2

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance: float):
        if balance < self.MINIMUM_BALANCE:
            raise exceptions.BalanceError(Message.MINIMUM_BALANCE_ERROR)
        self._balance = balance

    def __sub__(self, amount: float) -> None:
        """

        :param amount:
        :return:
        """

        self._balance -= amount

    def __add__(self, amount: float) -> None:
        """

        :param amount:
        :return:
        """

        self._balance += amount

    @abstractmethod
    def transfer(self, other: 'BankAccount', amount: float) -> None:
        """

        :param other:
        :param amount:
        :return:
        """
        pass

    @staticmethod
    def to_rial(amount: float):
        """

        :param amount:
        :return:
        """
        return amount * 10

    def __repr__(self):
        """

        :return:
        """
        data = vars(self)
        data['Rial'] = self.to_rial(self._balance)
        return str(data)

    def __str__(self):
        """

        :return:
        """
        return f'{self.owner_name}: {self._balance:,} Toman.'

    def __eq__(self, other: 'BankAccount'):
        """

        :param other:
        :return:
        """
        return self._balance == other._balance
