from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.config_reader import get_config


def test_add_coupon(driver, login):
    print("Login Successful")

    coupons_xpath = get_config('coupons','coupons')
    addcoupon_xpath = get_config('coupons','add_coupon')
    browse_xpath = get_config('coupons','browse')
    enter_product_xpath = get_config('coupons','enter_product')
    select_all_xpath = get_config('coupons','select_all')
    save_xpath = get_config('coupons','save')
    items_xpath = get_config('coupons','items')

    coupons = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, coupons_xpath)))
    coupons.click()

    addcoupon = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, addcoupon_xpath)))
    addcoupon.click()

    browse = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, browse_xpath)))
    ActionChains(driver).move_to_element(browse).perform()
    time.sleep(3)

    browse.click()

    enter_product = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, enter_product_xpath)))
    enter_product.send_keys('fruit')

    time.sleep(2)

    driver.find_element(By.XPATH, enter_product_xpath).send_keys(Keys.ENTER)

    time.sleep(3)
    items = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, items_xpath)))
    selected = len(items)
    print(selected)

    select_all = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, select_all_xpath)))
    select_all.click()

    save = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, save_xpath)))
    save.click()
    time.sleep(5)

    time.sleep(5)

    items_selected = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, items_xpath)))
    scroll_pixels = 500
    driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")
    time.sleep(3)
    applied = len(items_selected)
    print(applied)
    assert selected == applied

    print("Assertion successful")