from argparse import ArgumentParser
from user import User
from utils.user_utils import Utils
from utils import exceptions
from utils.messages import Message
from hashlib import sha256


def log_in(username: str, password: str) -> bool:
    """

    :param username:
    :param password:
    :return:
    """

    user = User.get_profile(username)

    if not user[username] != username or not user[password] != password:
        exceptions.SuperUserError(
            Message.WRONG_SUPERUSER_ERROR
        )


def main():
    """

    :return:
    """

    USERNAME = '382132701c4733c3402706cfdd3c8fc7f41f80a88dce5428d145259a41c5f12f'
    PASSWORD = '382132701c4733c3402706cfdd3c8fc7f41f80a88dce5428d145259a41c5f12f'
    superuser = User.create(
        USERNAME,
        PASSWORD,
        '1/1/1997',
    )

    parser = ArgumentParser(
        description="This script is implemented for admin access."
    )

    parser.add_argument('-u', '--username', metavar='USERNAME', required=True, type=str)
    parser.add_argument('-p', '--password', metavar='PASSWORD', required=True, type=str)
    parser.add_argument('-n', '--admin_username', metavar='ADMIN_USERNAME', required=True, type=str)
    parser.add_argument('-l', '--admin_password', metavar='ADMIN_PASSWORD', required=True, type=str)

    data = parser.parse_args()

    username = Utils.hashing_password(data.username)
    password = Utils.hashing_password(data.password)

    try:
        log_in(username, password)
    except exceptions.WRONG_SUPERUSER_ERROR as err:
        print(err)
    else:
        print('successssssssssss')


if __name__ == '__main__':
    main()
