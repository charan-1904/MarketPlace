import string
import pytest
import random
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def get_config(category, key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(category, key)


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver):
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


    # drop = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "(//span[@role = 'img'])[2]"))
    # )
    # drop.click()
    # print('sss')
    # sleep(10)
    # d= driver.find_element(By.XPATH,"((//span[@role = 'img'])[2]")
    # d.click()
    # sleep(10)
    # sleep(5)
    # driver.refresh()
    # sleep(5)
    #
    # user_dropdown = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "(//span[@role='img'])[1]"))
    # )
    #
    # # Click on the element
    # user_dropdown.click()
    # logout = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "(//li[@role = 'menuitem'])[8]"))
    # )
    # logout.click()
    # sleep(5)

@pytest.fixture(scope="module")
def SMP_login_invalid(driver):
    sleep(5)
    login_url = get_config("login", "url")
    driver.get(login_url)
    driver.maximize_window()
    sleep(5)

    username_invalid = get_config('info', 'username_invalid')
    password_invalid = get_config('info', 'password_invalid')

    username_xpath = get_config("login", "username_xpath")
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, username_xpath))
    )
    print("Username field found.")
    username_field.send_keys(username_invalid)

    password_xpath = get_config("login", "password_xpath")
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, password_xpath))
    )
    print("Password field found.")
    password_field.send_keys(password_invalid)
    login_button_xpath = get_config("login", "login_button_xpath")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, login_button_xpath))
    )
    print("Login button clickable.")
    login_button.click()
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[text()='Invalid Credentials']"))
    )
    # timeout_message = driver.find_element(By.XPATH,
    #                                       "//span[text()='Your login attempt timed out. Login will start from the beginning.']")
    expected_text = "Invalid Credentials"

        # Get the text of the element
    actual_text = error_message.text
    assert actual_text == expected_text

    print("Login with invalid credentials assertion passed!")

@pytest.fixture(scope="module")
def SMP_login_invalid_username(driver):
    sleep(5)
    login_url = get_config("login", "url")
    driver.get(login_url)
    driver.maximize_window()
    sleep(5)

    username_invalid = get_config('info', 'username_invalid')
    password_invalid = get_config('info', 'password')

    username_xpath = get_config("login", "username_xpath")
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, username_xpath))
    )
    print("Username field found.")
    username_field.send_keys(username_invalid)

    password_xpath = get_config("login", "password_xpath")
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, password_xpath))
    )
    print("Password field found.")
    password_field.send_keys(password_invalid)
    login_button_xpath = get_config("login", "login_button_xpath")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, login_button_xpath))
    )
    print("Login button clickable.")
    login_button.click()
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[text()='Invalid Credentials']"))
    )
    # timeout_message = driver.find_element(By.XPATH,
    #                                       "//span[text()='Your login attempt timed out. Login will start from the beginning.']")
    expected_text = "Invalid Credentials"

        # Get the text of the element
    actual_text = error_message.text
    assert actual_text == expected_text

    print("Login with invalid username assertion passed!")

@pytest.fixture(scope="module")
def SMP_login_invalid_password(driver):
    sleep(5)
    login_url = get_config("login", "url")
    driver.get(login_url)
    driver.maximize_window()
    sleep(5)

    username_invalid = get_config('info', 'username')
    password_invalid = get_config('info', 'password_invalid')

    username_xpath = get_config("login", "username_xpath")
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, username_xpath))
    )
    print("Username field found.")
    username_field.send_keys(username_invalid)

    password_xpath = get_config("login", "password_xpath")
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, password_xpath))
    )
    print("Password field found.")
    password_field.send_keys(password_invalid)
    login_button_xpath = get_config("login", "login_button_xpath")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, login_button_xpath))
    )
    print("Login button clickable.")
    login_button.click()
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[text()='Invalid Credentials']"))
    )
    # timeout_message = driver.find_element(By.XPATH,
    #                                       "//span[text()='Your login attempt timed out. Login will start from the beginning.']")
    expected_text = "Invalid Credentials"

        # Get the text of the element
    actual_text = error_message.text
    assert actual_text == expected_text

    print("Login with invalid password assertion passed!")

# @pytest.fixture(scope="module")
# def login_(driver):
#     login_url = get_config("login", "url")
#     driver.get(login_url)
#     driver.maximize_window()
#
#     username = get_config('info', 'username')
#     password = get_config('info', 'password')
#
#     print("Waiting for username field...")
#     username_xpath = get_config("login", "username_xpath")
#     username_field = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, username_xpath))
#     )
#     print("Username field found.")
#     username_field.send_keys(username)
#
#     print("Waiting for password field...")
#     password_xpath = get_config("login", "password_xpath")
#     password_field = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, password_xpath))
#     )
#     print("Password field found.")
#     password_field.send_keys(password)
#     login_button_xpath = get_config("login", "login_button_xpath")
#     login_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, login_button_xpath))
#     )
#     print("Login button clickable.")
#     login_button.click()
#
#     print("Waiting for URL change after login...")
#     WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
#     print("URL changed.")
#     # sleep(5)
#     driver.refresh()
#     sleep(5)
#
#     user_dropdown = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "(//span[@role='img'])[1]"))
#     )
#
#     # Click on the element
#     user_dropdown.click()
#     logout = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "(//li[@role = 'menuitem'])[8]"))
#     )
#     logout.click()
#     sleep(5)

@pytest.fixture(scope="module")
def generate_random():
    prefix = "_test_"
    suffix = ''.join(random.choices(string.digits, k=3))
    random_text = prefix + suffix
    return random_text