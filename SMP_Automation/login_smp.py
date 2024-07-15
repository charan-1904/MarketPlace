from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser
from _testinternalcapi import get_config
from time import sleep



# Initialize WebDriver
driver = webdriver.Chrome()




def get_config(category, key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(category, key)

def SMP_login_valid(username,password):
    driver = webdriver.Chrome()

    login_url = get_config("login", "url")
    driver.get(login_url)
    driver.maximize_window()
    sleep(5)  # Give time for the page to load

    username = username
    password = password

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

    # Wait for the page to load after login
    print("Waiting for URL change after login...")
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    print("URL changed.")
    driver.refresh()
    sleep(5)

    # user_dropdown = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "(//span[@role='img'])[1]"))
    # )
    #
    # # Click on the element
    # user_dropdown.click()
    # logout = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "(//li[@role = 'menuitem'])[9]"))
    # )
    # logout.click()
    # sleep(5)

def SMP_login_invalid(username,password):
    sleep(5)
    login_url = get_config("login", "url")
    driver.get(login_url)
    driver.maximize_window()
    sleep(5)

    username_invalid = username
    password_invalid = password

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
