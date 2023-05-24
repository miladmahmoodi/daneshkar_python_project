from abc import ABC,abstractmethod

class BankAccount:

    def __init__(self, owner_name: str, cvv2: str, password: str, balance: float) -> None:
        """
        Initializes a Bank account
        Args:
            owner_name (str): The name that has Bank's Account
            cvv2 (str): The cvv2 of Bank account
            password (str): the password of bank account
            balance (float): The initial account balance
        """
        self.owner_name = owner_name
        self.__balance = balance
        self.__password = password
        self.cvv2 = cvv2

    def __sub__(self, amount: float) -> None:
        """
        Subtracts amount from bank account
        Args:
            amount (float): The amount to subtract from the bank account
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")


    def __add__(self, amount: float) -> None:
        """
        Add amount to the balance account
        Args:
            amount (float): The amount to add to the bank account
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        self.__balance += amount


    @abstractmethod
    def transfer(self, amount: float, destination_account: str) -> None:
        """
        Transfer an amount to another bank account
        Args:
            amount (float): The amount to transfer
            destination_account (str): The destination account for the transfer
        """
        if amount <= 0:
            raise ValueError("The amount cannot be zero")
        if self.__balance < amount:
            raise ValueError("Insufficient funds for transfer")
        

    def __repr__(self) -> str:
        """
        Representing the Bank account
        """
        return f"The owner of bank account: {self.owner_name}, and Balance: {self.__balance}"
    

    def __str__(self) -> str:
        """
        Representing the bank information
        """
        return f"Bank Account Information: Owner Name: {self.owner_name}, Balance: {self.__balance}"