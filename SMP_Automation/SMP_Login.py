import time
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _testinternalcapi import get_config
from configparser import ConfigParser
# from login import SMP_login_valid
from login_smp import SMP_login_valid,SMP_login_invalid


# def test_SMP_login(login):
#     # usernames = get_config("info", "username_list").split(',')
#     # for username in usernames:
#     #     print(product_type)
#     print("Login is successful")
#     assert login is None, "Login fixture failed"
#
# def test_SMP_Invalidlogin(SMP_login_invalid):
#     # Test the login fixture
#     assert SMP_login_invalid is None, "test case with invalid credentials failed"
#
# def test_SMP_Invalid_Username_login(SMP_login_invalid_username):
#     assert SMP_login_invalid_username is None, "Test case with invalid username failed"
#
# def test_SMP_Invalid_Password_login(SMP_login_invalid_password):
#     assert SMP_login_invalid_password is None, "Test case with invalid password failed"

# username_list=['charan','test']
# password_list=['Charan@19042002','test']


def get_config(category, key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(category, key)


# def test_SMP_login():
#     username_list = get_config("info", "username_list").split(',')
#     password_list = get_config("info", "password_list").split(',')
#     # print(usernames[0])
#
#
#
#     for username in username_list:
#         for password in password_list:
#             if username == username_list[0] and password == password_list[0]:
#                 SMP_login_valid(username, password)
#             else:
#                 SMP_login_invalid(username, password)


def test_SMP_login_valid():
    username_list = get_config("info", "username_list").split(',')
    password_list = get_config("info", "password_list").split(',')

    valid_username = username_list[0]
    valid_password = password_list[0]

    SMP_login_valid(valid_username, valid_password)


def test_SMP_login_invalid():
    username_list = get_config("info", "username_list").split(',')
    password_list = get_config("info", "password_list").split(',')

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
