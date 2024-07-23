import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.config_reader import get_config


def test_dashboardCount(driver,login):
    print('login successful')
    prod_temp = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('dashboard','product_templates'))))
    print("No. of Product Templates:", prod_temp.text.strip().replace('\n', ' '))

    prod_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, get_config('dashboard', 'prod_div'))))
    #iteratewithin the div class
    items = prod_div.find_elements(By.XPATH, ".//main[@class='ant-layout-content mt-3 flex space-x-16  css-w3qpxn']")

    for item in items:
        print(item.text.strip())

    products = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('dashboard','products'))))
    print("No. of Products:", products.text.strip().replace('\n', ' '))

    vendors = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('dashboard','vendors'))))
    print("No. of Vendors:", vendors.text.strip().replace('\n', ' '))


    recent_orders = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,get_config('dashboard','recent_orders'))))

    #
    # for order in recent_orders:
    #     print(order.text.strip())
    print("No.of Recent Orders:",len(recent_orders))
    order_ids = []

    for order in recent_orders:

        order_id_element = order.find_element(By.XPATH, ".//td[1]/h1")
        driver.execute_script("arguments[0].scrollIntoView();", order_id_element)
        order_id = order_id_element.text.strip()
        order_ids.append(order_id)
    print("Order IDs:",order_ids)


    categories = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,get_config('dashboard','categories'))))
    print("No.of Categories:",len(categories))
    categories_names=[]

    for category in categories:

        name = category.find_element(By.XPATH,".//td[1]/main/span")
        driver.execute_script("arguments[0].scrollIntoView();", name)

        name_element = name.text.strip()
        categories_names.append(name_element)

    print("Top Categories:",categories_names)


