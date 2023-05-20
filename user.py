#! /usr/bin/python3

"""
This module create for manage users.
"""

from utils.user_utils import Utils
from utils.exceptions import *
from utils.messages import Message


class User:
    """
    A class used to represent User.
    """
    __profiles = {}

    def __init__(self, username: str, password: str, phone_number: str | None = None):
        self.id = Utils.id_generator()
        self.__username = username
        self.phone_number = phone_number
        self.__password = password

    def sign_in(self, password: str) -> 'User':
        """
        Sign in the user with the given password.

        :param password: A string representing the password of the user.
        :return: The instance of User.
        :raises ValueError: If the given password is wrong.
        """

        password = Utils.hashing_password(password)

        if self.__password != password:
            raise SigninError(Message.WRONG_USERNAME_PASSWORD)

        return self

    def update_username(self, username: str) -> 'User':
        """
        Update the username of the user.

        :param username: A string representing the new username.
        :return: The instance of User.
        :raises ValueError: If the given username already exists.
        """
        if self.__username == username:
            raise NotChangeUsername(Message.NOT_CHANGE_USERNAME_MESSAGE)

        username = type(self).check_username(username)

        old_username = self.__username
        del type(self).__profiles[old_username]

        self.__username = username
        type(self).__profiles[username] = self

        return self

    def update_phone_number(self, phone_number: str) -> 'User':
        """
        Update the phone number of the user.

        :param phone_number: A string representing the new phone_number.
        :return: The instance of User.
        """

        phone_number = Utils.check_phone_number(phone_number)

        self.phone_number = phone_number

        return self

    def save(self) -> 'User':
        """
        Saves the user profile to the class private variable `profiles` with the username key.

        :return: None
        """
        type(self).__profiles[self.__username] = self
        return self

    @staticmethod
    def check_username(username: str) -> str:
        if not Utils.is_valid_username(username):
            raise WrongUserName(Message.WRONG_USERNAME)

        if User.exists_user(username):
            raise ExistsUserError(Message.EXIST_USER_MESSAGE)

        return username

    @staticmethod
    def get_profile(username: str) -> 'User':
        """
        Returns the profile of the user with the given username.

        :param username: str, the username of the user.
        :return: the profile of the user.
        :raises: ExistsUserError, if the user with the given username does not exist.
        """

        if not User.exists_user(username):
            raise ExistsUserError(Message.NOT_EXIST_USER_MESSAGE)

        return User.__profiles[username]

    @staticmethod
    def exists_user(username: str) -> bool:
        """
        Check whether the given username exists in the profiles list.

        :param username: A string representing the username to be checked.
        :return: True if the username exists in the profiles list, False otherwise.
        """

        return username in User.__profiles

    def update_password(self, old_password: str, new_password: str, confirm_password: str) -> 'User':
        """
        Update the password of the user.

        :param old_password: A string representing the old password.
        :param new_password: A string representing the new password.
        :param confirm_password: A string representing the new password confirmation.
        :return: The instance of User.
        :raises ValueError: If the given old password is wrong.
        :raises Exception: If the new password doesn't match the confirmation.
        """

        old_password = Utils.hashing_password(old_password)

        if self.__password != old_password:
            raise PasswordError(Message.WRONG_PASSWORD)

        if new_password != confirm_password:
            raise ConfirmPasswordError(Message.NOT_MATCH_PASSWORD)

        self.__password = Utils.check_password(new_password)

        return self

    @classmethod
    def create(cls, username: str, password: str, phone_number: str = None) -> 'User':
        """
        Create a new user profile with the given username, phone_number, and password.

        :param username: A string representing the username.
        :param phone_number: A string representing the phone number.
        :param password: A string representing the password.
        :return: If the input is valid, return a new instance of User. Otherwise, return an Exception object.
        """

        username = cls.check_username(username)
        password = Utils.check_password(password)
        phone_number = Utils.check_phone_number(phone_number)

        profile = cls(
            username,
            password,
            phone_number=phone_number,
        ).save()

        if not cls.exists_user(username):
            return NotExistsUserError(Message.SOMETHING_WRONG)

        return profile

    def __str__(self) -> str:
        """
        Return the string representation of the User object.

        :return: A string representing the User object.
        """
        return f"\033[95m----------------------------------------------------------------------\n" \
               f"Hi dear '{self.__username}'. Hope you are well :)\n" \
               f"Your id is '{self.id}' and your phone number is '{self.phone_number}'\n" \
               f"----------------------------------------------------------------------\033[00m"
