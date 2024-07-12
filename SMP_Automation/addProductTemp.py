import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from _testinternalcapi import get_config
from configparser import ConfigParser
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

def get_config(category, key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(category, key)

def test_addTemp(driver,login,generate_random):

    print("Login Successful")
    products_xpath = get_config("product_temp", "products")
    products_temp_xpath = get_config('product_temp',"product_template")
    add_prod = get_config('product_temp',"add_product")
    temp_name = get_config('product_temp', 'temp_name')
    desc_name = get_config('product_temp', 'desc')
    # prod_type = get_config('product_temp', 'type')
    digital = get_config('product_temp', 'digital')
    physical = get_config('product_temp','physical')
    subscription = get_config('product_temp', 'subscription')
    bundled = get_config('product_temp','bundled')
    save = get_config('templates','save_xpath')
    # product_types = [
    #             get_config('product_temp', 'digital'),
    #             get_config('product_temp', 'physical'),
    #             get_config('product_temp', 'subscription'),
    #             get_config('product_temp', 'bundled'),
    #             # get_config('product_temp', 'service')
    #         ]

    drop_down = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, products_xpath))
    )
    drop_down.click()
    # driver.find_element(By.XPATH,products_temp_xpath).click()
    prod_temp = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, products_temp_xpath))

    )
    prod_temp.click()

    add_prod = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, add_prod))

    )
    add_prod.click()
    template_name_field = get_config('templates', 'template_name').split(',')


    template_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, temp_name))

    )
    template_name.send_keys(template_name_field[0]+generate_random)

    description = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, desc_name))

    )
    description.send_keys('description')
    time.sleep(2)
    temp_type = driver.find_element(By.XPATH,"//div[@class='ant-select add-product-template-select-add !min-w-[100%] css-bvjycy ant-select-multiple ant-select-allow-clear ant-select-show-arrow']")
    temp_type.click()

    digital_type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, digital))
    )

    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView();", digital_type)

    # Wait until the element is clickable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, digital))
    )

    # Click the digital_type
    digital_type.click()
    time.sleep(5)
    temp_type.click()
    save = driver.find_element(By.XPATH,save).click()
    time.sleep(5)

    drop_hover = driver.find_element(By.XPATH, "(//span[text()='Draft'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(drop_hover).perform()
    time.sleep(2)
    submit = driver.find_element(By.XPATH,"//span[text()='Submit For Approval']")
    submit.click()
    reason = driver.find_element(By.XPATH,'//*[@placeholder="Please enter submission request message"]')
    reason.send_keys("Approve")
    time.sleep(2)
    ok = driver.find_element(By.XPATH,"//*[text() = 'Ok']")
    ok.click()
    time.sleep(5)


    time.sleep(5)


    assert login is None, "Login fixture failed"


# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from configparser import ConfigParser
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# def get_config(category, key):
#     config = ConfigParser()
#     config.read("config.ini")
#     return config.get(category, key)
#
#
# def test_addTemp(driver, login, generate_random):
#     print("Login Successful")
#
#     products_xpath = get_config("product_temp", "products")
#     products_temp_xpath = get_config('product_temp', "product_template")
#     add_prod = get_config('product_temp', "add_product")
#     temp_name = get_config('product_temp', 'temp_name')
#     desc_name = get_config('product_temp', 'desc')
#     save = get_config('templates', 'save_xpath')
#
#     template_names = get_config('templates', 'template_name').split(',')
#     product_types = [
#         get_config('product_temp', 'digital'),
#         get_config('product_temp', 'physical'),
#         get_config('product_temp', 'subscription'),
#         get_config('product_temp', 'bundled'),
#         # get_config('product_temp', 'service')
#     ]
#
#     for template_name in template_names:
#         drop_down = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, products_xpath))
#         )
#         drop_down.click()
#
#         prod_temp = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, products_temp_xpath))
#         )
#         prod_temp.click()
#
#         add_prod_element = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, add_prod))
#         )
#         add_prod_element.click()
#
#         template_input = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, temp_name))
#         )
#         template_input.send_keys(template_name + generate_random)
#
#         description_input = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, desc_name))
#         )
#         description_input.send_keys('description')
#         time.sleep(2)
#
#         temp_type = driver.find_element(By.XPATH,
#                                         "//div[@class='ant-select add-product-template-select-add !min-w-[100%] css-bvjycy ant-select-multiple ant-select-allow-clear ant-select-show-arrow']")
#         temp_type.click()
#
#         for product_type in product_types:
#             digital_type = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, product_type))
#             )
#
#             driver.execute_script("arguments[0].scrollIntoView();", digital_type)
#             WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, product_type))
#             ).click()
#
#             time.sleep(5)
#
#             temp_type.click()
#             driver.find_element(By.XPATH, save).click()
#             time.sleep(5)
#
#             drop_hover = driver.find_element(By.XPATH, "(//span[text()='Draft'])[1]")
#             actions = ActionChains(driver)
#             actions.move_to_element(drop_hover).perform()
#             time.sleep(2)
#             submit = driver.find_element(By.XPATH, "//span[text()='Submit For Approval']")
#             submit.click()
#
#             reason = driver.find_element(By.XPATH, '//*[@placeholder="Please enter submission request message"]')
#             reason.send_keys("Approve")
#             time.sleep(2)
#
#             ok = driver.find_element(By.XPATH, "//*[text() = 'Ok']")
#             ok.click()
#             time.sleep(5)
#             # driver.quit()
#
#     assert login is None, "Login fixture failed"
