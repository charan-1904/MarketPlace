from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from utils.config_reader import get_config



def test_assignOrders(driver, vendor_login):
    print("Login Successful")

    orders_xpath = get_config('orders', 'orders')
    received_xpath = get_config('orders', 'received')
    page_xpath = get_config('orders', 'page')
    change_page_xpath = get_config('orders', 'change_page')
    items_xpath = get_config('orders','items')
    assign_xpath = get_config('orders','assign')
    alert_xpath = get_config('orders','alert')
    time.sleep(3)

    orders = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, orders_xpath)))
    orders.click()

    received = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, received_xpath)))
    received.click()

    page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, page_xpath)))
    ActionChains(driver).move_to_element(page).perform()
    page.click()

    change_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, change_page_xpath)))
    change_page.click()
    time.sleep(2)

    items = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, items_xpath)))
    items_count = len(items)

    print("No. of items to be assigned:",items_count)

    for i in range(4):


        assign = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, assign_xpath)))
        assign.click()


        alert_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, alert_xpath)))

        alert_text = alert_element.text.strip()

        expected_message = "Order item has been successfully assigned"
        print(alert_text)

        assert expected_message in alert_text
        print("assertion passed")


        time.sleep(3)


