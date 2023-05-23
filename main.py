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


def sign_in() -> None:
    """
    Display a form for user sign-in.

    The function prompts the user to enter their username and password.
    If the username and password are correct, the function displays a menu with options to view the user profile, edit
    the user profile, change the user password, or logout.
    If the username or password is incorrect, the function raises a ValueError.

    :return: None.
    """

    print(Message.SIGNIN_TITLE_PROMPT)
    username = input(Message.SIGNIN_USERNAME_INPUT_PROMPT)
    password = getpass(Message.SIGNIN_PASSWORD_INPUT_PROMPT)

    try:
        profile = User.get_profile(username)
        profile.sign_in(password)
    except ExistsUserError as err:
        print(err)
    except SigninError as err:
        print(err)
    else:
        print(Message.welcome_user_message(username))

        while True:
            print(Message.MENU_SIGNIN_PROMPT)
            signin_inp = input(Message.MENU_SIGNIN_SELECTED_ITEM_PROMPT)

            match signin_inp:
                case '1':
                    print(profile)
                case '2':
                    update_profile(profile)
                case '3':
                    update_password(profile)
                case '4':
                    manage_bank(profile)
                case '5':
                    wallet(profile)
                case '6':
                    break


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