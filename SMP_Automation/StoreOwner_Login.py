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


def get_config(category, key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(category, key)


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