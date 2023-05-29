#! /usr/bin/python3

"""
This module defines custom exception classes for a user authentication system.
"""


class ExistsUserError(Exception):
    """
    Raised when a user with the given username already exists.
    """
    pass


class NotExistsUserError(Exception):
    """
    Raised when a user with the given username does not exist.
    """
    pass


class SigninError(Exception):
    """
    Raised when there is an error during the sign-in process.
    """
    pass


class PasswordError(Exception):
    """
    Raised when the password provided is invalid.
    """
    pass


class ConfirmPasswordError(Exception):
    """
    Raised when the passwords don`t match.
    """
    pass


class WrongPhoneNumber(Exception):
    """
    Raised when the phone number don`t match with regex.
    """
    pass


class WrongUserName(Exception):
    """
    Raised when the username empty or null.
    """
    pass


class NotChangeUsername(Exception):
    """
    Raised when the username not changed.
    """
    pass


class NoSalonFound(Exception):
    """
    Raised when there is no salon with that name
    """
    pass


class SameSalonFound(Exception):
    pass


class ZeroCapacityError(Exception):
    pass
 
class WrongDateValue(Exception):
    """
    """
    pass

class ShowDoesNotExist(Exception):
    """
    Raised when the show does not exist.
    """
    pass


class SuperUserError(Exception):
    """

    """
    pass


class BalanceError(Exception):
    """

    """
    pass


class Cvv2PasswordError(Exception):
    """

    """
    pass
