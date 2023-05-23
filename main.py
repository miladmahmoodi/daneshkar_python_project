from user import User
from utils.exceptions import *
from getpass import getpass
from utils.messages import Message


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
