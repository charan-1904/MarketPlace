import string
import pytest
import random
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from utils.config_reader import get_config
from utils.config import Config

@pytest.fixture(scope="session")
def config():
    # Assuming config.ini is in the project root directory
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.ini'))
    return Config(config_path)


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver):
    login_url = get_config("login", "url")
    driver.get(login_url)
    driver.maximize_window()

    username = get_config('info', 'storeowner_username')
    password = get_config('info', 'storeowner_password')
    print(username)

    print("Waiting for username field...")
    username_xpath = get_config("login", "username_xpath")
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, username_xpath))
    )
    print("Username field found.")
    username_field.send_keys(username)

    print("Waiting for password field...")
    password_xpath = get_config("login", "password_xpath")
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, password_xpath))
    )
    print("Password field found.")
    password_field.send_keys(password)
    login_button_xpath = get_config("login", "login_button_xpath")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, login_button_xpath))
    )
    print("Login button clickable.")
    login_button.click()

    print("Waiting for URL change after login...")
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    print("URL changed.")

@pytest.fixture(scope="module")
def vendor_login(driver):
    login_url = get_config("login", "vendor_url")
    driver.get(login_url)
    driver.maximize_window()

    username = get_config('info', 'vendor_username')
    password = get_config('info', 'vendor_password')
    print(username)

    print("Waiting for username field...")
    username_xpath = get_config("login", "username_xpath")
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, username_xpath))
    )
    print("Username field found.")
    username_field.send_keys(username)

    print("Waiting for password field...")
    password_xpath = get_config("login", "password_xpath")
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, password_xpath))
    )
    print("Password field found.")
    password_field.send_keys(password)
    login_button_xpath = get_config("login", "login_button_xpath")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, login_button_xpath))
    )
    print("Login button clickable.")
    login_button.click()

    print("Waiting for URL change after login...")
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    print("URL changed.")


@pytest.fixture(scope="module")
def generate_random():
    prefix = "_test_"
    suffix = ''.join(random.choices(string.digits, k=3))
    random_text = prefix + suffix
    return random_text