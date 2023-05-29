#! /usr/bin/python3

import pickle
from bank_account import BankAccount
from utils import exceptions
from utils.messages import Message


class Bank(BankAccount):
    __MINIMUM = 10_000
    transfer_fee = 600
    __accounts = dict()

    def __init__(self, owner_name: str, cvv2: str, password: str, balance: float) -> None:
        super().__init__(owner_name, balance)
        self.cvv2 = cvv2
        self.password = password
        type(self).__accounts[self.owner_name] = self
        type(self).save()


    def __add__(self, amount: float):
        """

        :param amount:
        :return:
        """

        account_data = self.get_bank_account(self.owner_name)

        if account_data['cvv2'] != self.cvv2 and account_data['password'] != self.password:
            raise exceptions.CVV2_PASSWORD_ERROR(Message.WRONG_CVV2_PASSWORD)

        if self._balance + amount < self.__MINIMUM:
            raise exceptions.BalanceError(Message.MINIMUM_BALANCE_ERROR)

        super().__add__(amount)
    
    def TRANSFER_FEE(self, amount):
        """
        The fee that is deducted from the user's account for each transfer
        and if it is more than 1 milion if will reduce 1000 toman from balance 
        """
        if amount > 10_000_000:
            return self.__balance - 1_000
        return self.__balance - 600
    
    def __sub__(self, amount: float):
        """

        :param amount:
        :return:
        """

        account_data = self.get_bank_account(self.owner_name)

        if account_data['cvv2'] != self.cvv2 and account_data['password'] != self.password:
            raise exceptions.Cvv2PasswordError(Message.WRONG_CVV2_PASSWORD)

        if self._balance - amount < self.__MINIMUM:
            raise exceptions.BalanceError(Message.MINIMUM_BALANCE_ERROR)

        super().__sub__(amount)

    def transfer(self, other: 'BankAccount', amount: float):
        if amount < 0: 
            raise exceptions.BalanceError(Message.MINIMUM_BALANCE_ERROR)

        self.__sub__(amount - type(self).transfer_fee)
        other.__add__(amount)

    @classmethod
    def save(cls) -> None:
        """

        :return:
        """

        with open('database/bank.pickle', 'wb') as file:
            pickle.dump(cls.__accounts, file)
        cls.__accounts.clear()

    @classmethod
    def load(cls) -> dict:
        """

        :return:
        """

        with open('database/bank.pickle', 'rb') as file:
            return pickle.load(file)

    def get_bank_account(self, owner_name: str) -> dict:
        """

        :param owner_name:
        :return:
        """

        accounts_data = type(self).load()
        return accounts_data[owner_name]
