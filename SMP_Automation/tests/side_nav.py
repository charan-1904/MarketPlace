import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from configparser import ConfigParser
from _testinternalcapi import get_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.config_reader import get_config


driver = webdriver.Chrome()

def test_side_navbar():
        login_url = get_config("login", "url")
        driver.get(login_url)
        driver.maximize_window()
        sleep(5)  # Give time for the page to load

        # Read configuration values
        username = get_config('info', 'username')
        password = get_config('info', 'password')

        # Explicitly wait for the username field to be visible
        print("Waiting for username field...")
        username_xpath = get_config("login", "username_xpath")
        username_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, username_xpath))
        )
        print("Username field found.")
        username_field.send_keys(username)

        # Explicitly wait for the password field to be visible
        print("Waiting for password field...")
        password_xpath = get_config("login", "password_xpath")
        password_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, password_xpath))
        )
        print("Password field found.")
        password_field.send_keys(password)

        # Explicitly wait for the login button to be clickable
        print("Waiting for login button...")
        login_button_xpath = get_config("login", "login_button_xpath")
        login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, login_button_xpath))
        )
        print("Login button clickable.")
        login_button.click()
        print("Waiting for URL change after login...")
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
        print("URL changed.")
        wait = WebDriverWait(driver, 10)
        elements = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[@class='ant-menu-title-content']")))
        element_texts = []
        for element in elements:
            element_texts.append(element.text)
        print("List of elements in the side navbar:\n",element_texts)


