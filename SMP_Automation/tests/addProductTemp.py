from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.config_reader import get_config


def test_addTemp(driver, vendor_login, generate_random):
    print("Login Successful")

    products_xpath = get_config("product_temp", "products")
    products_temp_xpath = get_config('product_temp', "product_template")
    add_prod = get_config('product_temp', "add_product")
    temp_name = get_config('product_temp', 'temp_name')
    desc_name = get_config('product_temp', 'desc')
    save = get_config('templates', 'save_xpath')
    back_xpath = get_config('templates','back')
    template_names = get_config('templates', 'template_name').split(',')
    product_types = [
        get_config('product_temp', 'digital'),
        get_config('product_temp', 'physical'),
        get_config('product_temp', 'subscription'),
        get_config('product_temp', 'bundled'),
    ]

    drop_down = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, products_xpath))
    )
    drop_down.click()

    prod_temp = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, products_temp_xpath))
    )
    prod_temp.click()

    for template_name in template_names:
        time.sleep(5)


        add_prod_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, add_prod))
        )
        add_prod_element.click()

        template_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, temp_name))
        )
        template_input.send_keys(template_name + generate_random)

        description_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, desc_name))
        )
        description_input.send_keys('description')
        time.sleep(2)

        temp_type = driver.find_element(By.XPATH,
                                        "(//div[@class='ant-select-selector'])[3]")
        temp_type.click()
        time.sleep(2)

        print('clicked')


        print(type(product_types[0]))
        if 'digital' in template_name:
            product_type = product_types[0]
        elif 'physical' in template_name:
            product_type = product_types[1]
        elif 'subscription' in template_name:
            product_type = product_types[2]
        elif 'bundled' in template_name:
            product_type = product_types[3]

        time.sleep(3)
        print('type selected')

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, product_type))
        )
        print('element found')
        ActionChains(driver).move_to_element(element).perform()
        print('element scrolled')




        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, product_type))
        ).click()


        time.sleep(5)

        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ESCAPE)
        driver.find_element(By.XPATH, save).click()
        time.sleep(5)

        drop_hover = driver.find_element(By.XPATH, "(//span[text()='Draft'])[1]")
        actions = ActionChains(driver)
        actions.move_to_element(drop_hover).perform()
        time.sleep(2)
        submit = driver.find_element(By.XPATH, "//span[text()='Submit For Approval']")
        submit.click()

        reason = driver.find_element(By.XPATH, '//*[@placeholder="Please enter submission request message"]')
        reason.send_keys("Approve")
        time.sleep(2)

        ok = driver.find_element(By.XPATH, "//*[text() = 'Ok']")
        ok.click()
        time.sleep(2)
        back = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,back_xpath)))
        back.click()

        time.sleep(5)


    assert vendor_login is None, "Login fixture failed"

