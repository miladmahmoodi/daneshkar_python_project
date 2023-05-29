import json
from argparse import ArgumentParser
from user import User
from utils import user_utils, exceptions
from utils.messages import Message
from hashlib import sha256


def main():
    USERNAME = '382132701c4733c3402706cfdd3c8fc7f41f80a88dce5428d145259a41c5f12f'
    PASSWORD = '382132701c4733c3402706cfdd3c8fc7f41f80a88dce5428d145259a41c5f12f'

    # bank for superuser to transfer cost of subscription

    parser = ArgumentParser(
        description="This script is implemented for admin access."
    )

    parser.add_argument('-u', '--username', metavar='USERNAME', required=True, type=str)
    parser.add_argument('-p', '--password', metavar='PASSWORD', required=True, type=str)
    parser.add_argument('-n', '--name', metavar='NAME', required=True, type=str)
    parser.add_argument('-l', '--location', metavar='LOCATION', required=True, type=str)

    data = parser.parse_args()

    username = sha256(
        data.username.encode()
    ).hexdigest()

    password = sha256(
        data.password.encode()
    ).hexdigest()

    if not username != USERNAME or not password != PASSWORD:
        exceptions.SuperUserError(
            Message.WRONG_SUPERUSER_ERROR
        )


if __name__ == '__main__':
    main()
