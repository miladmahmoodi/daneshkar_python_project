#! /usr/bin/python3


from abc import ABC
import pickle
from tkinter import SEL_FIRST
from bank_acoount import BankAccount


class Bank(BankAccount, ABC): 
    __MINIMUM = 10_000 
    __accounts = []
    
    def __init__(self, owner, balance) -> None:
        super().__init__(owner, balance)
        type(self).__accounts.append(self) 


    def create_account(self, account_number:str, balance:float, password:str, cvv2:str):
        """
        creating different bank acccount
        """
        new_account = BankAccount(account_number, balance, password, cvv2)
        self.accounts.append(new_account)
        return f"New account {account_number} created for {self.name}."
    

    
    def select_account(self):
        """
        selecting different account and return that
        """
        print("Select your account:")
        for i, account in enumerate(self.accounts):
            return f"{i+1}. Account {account.account_number} ({account.balance})"
        account_choice = int(input("Enter account number: "))
        return self.accounts[account_choice - 1]


    def __add__(self, amount:int):
        """
        addig amount of money and checking balance to be more than minimum
        """
        if self.amoumt < 0:
            raise ValueError('Invalid amount')
        if self.__balance + amount < self.__MINIMUM: 
            raise ValueError('Invalid balance')
        return type(self).__add__(amount)
    
    def TRANSFER_FEE(self, amount):
        """
        The fee that is deducted from the user's account for each transfer
        and if it is more than 1 milion if will reduce 1000 toman from balance 
        """
        if amount > 10_000_000:
            return self.__balance - 1_000
        return self.__balance - 600
    
    def __sub__(self, amount):
        if self.__balance - amount < self.__MINIMUM: 
            raise ValueError('Invalid balance')
        return type(self).__sub__(amount)
    

    def transfer(self, Admin: 'BankAccount', amount: int):
        if amount < 0: 
            raise ValueError('Invalid amount')
        self - TRANSFER_FEE(self)
        Admin + amount  
            
        
    @classmethod
    def save(cls):
        with open('account_pickle', 'wb')as file:
            pickle.dump(cls.__accounts, file)

    @classmethod
    def load(cls):
        with open('account_pickle', 'rb')as file:
            cls.__accounts.extend(pickle.load(file))

        










