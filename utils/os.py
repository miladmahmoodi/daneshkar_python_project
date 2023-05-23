"""
Clear the terminal screen based on the operating system.
"""

import os
import platform


def clear_terminal() -> None:
    """
    Clear the terminal screen based on the operating system.

    :return None
    """

    current_os_name = platform.system()

    match current_os_name:
        case 'Linux' | 'Darwin':
            os.system('clear')
        case 'Windows':
            os.system('cls')
