import pytest
from _testinternalcapi import get_config
from login_smp import SMP_login_valid,SMP_login_invalid
from utils.config_reader import get_config


def test_SMP_login_valid():
    username_list = get_config("info", "storeowner_username_list").split(',')
    password_list = get_config("info", "storeowner_password_list").split(',')

    valid_username = username_list[0]
    valid_password = password_list[0]

    SMP_login_valid(valid_username, valid_password)


def test_SMP_login_invalid():
    username_list = get_config("info", "storeowner_username_list").split(',')
    password_list = get_config("info", "storeowner_password_list").split(',')

    valid_username = username_list[0]
    valid_password = password_list[0]

    for username in username_list:
        for password in password_list:
            if username != valid_username or password != valid_password:
                SMP_login_invalid(username, password)

        for username in username_list:
            if username != valid_username:
                SMP_login_invalid(username, valid_password)

        for password in password_list:
            if password != valid_password:
                SMP_login_invalid(valid_username, password)


if __name__ == "__main__":
    pytest.main()