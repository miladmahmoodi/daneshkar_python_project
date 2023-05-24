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

