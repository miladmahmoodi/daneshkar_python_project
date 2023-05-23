from user import User
from utils.exceptions import *
from getpass import getpass
from utils.messages import Message
from datetime import datetime


def sign_up():
    """
    Display a form for signup a new user.

    The function prompts the user to enter their username, phone number, and password.
    Once the information is provided, the function calls the 'create' method of the 'User' class to create a new user.
    If the user is created successfully, a message is printed to the console.

    :return: Success message or Error message.
    """

    print(Message.SIGNUP_TITLE_PROMPT)
    username = input(Message.USERNAME_INPUT_PROMPT)
    password = getpass(Message.PASSWORD_INPUT_PROMPT)
    phone_number = input(Message.PHONE_NUMBER_INPUT_PROMPT)
    birth_date = input(Message.BIRTH_DATE_INPUT_PROMPT)
    birth_date = datetime.strptime(birth_date, '%d-%m-%Y')

    try:
        User.create(
            username,
            password,
            birth_date,
            # phone_number=phone_number,
        )
    except WrongUserName as err:
        print(err)
    except ExistsUserError as err:
        print(err)
    except NotExistsUserError as err:
        print(err)
    except WrongPhoneNumber as err:
        print(err)
    except PasswordError as err:
        print(err)
    else:
        print(Message.success_signup(username))


def main() -> None:
    """
    Display the main menu.

    The function displays a menu with options to end the process, sign up, or sign in.
    If the user selects sign up, the function calls the 'sign_up' function to register a new user.
    If the user selects sign in, the function calls the 'sign_in' function to authenticate the user.

    :return: None.
    """

    while True:
        print(Message.MENU_MAIN_PROMPT)
        inp = input(Message.MENU_MAIN_SELECTED_PROMPT)
        match inp:
            case '0':
                break
            case '1':
                sign_up()
            case '2':
                sign_in()


if __name__ == '__main__':
    main()
