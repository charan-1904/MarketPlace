from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from utils.config_reader import get_config


def test_addPolicy(driver,login,generate_random):
    print('login successful')

    settings = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('settings','settings'))))
    settings.click()

    policy_settings = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('settings','policies'))))
    policy_settings.click()
    time.sleep(5)
    add_policy = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,get_config('settings','add_policy'))))
    add_policy.click()

    policy_title = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('settings','policy_title'))))
    policy_title_input = 'New_Policy'+generate_random
    print(policy_title_input)
    policy_title.send_keys(policy_title_input)


    policy_description_items = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,get_config('settings','description'))))
    final_description = len(policy_description_items)
    print(final_description)
    policy_description = driver.find_element(By.XPATH,f"(//div[@data-placeholder='Enter policy text here'])[{final_description-1}]")
    policy_description.send_keys('Policy_Description')
    time.sleep(5)
    save = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,get_config('settings','save'))))
    save.click()
    time.sleep(5)

    publish_items = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,get_config('settings','publish'))))
    publish_count = len(publish_items)
    print(publish_count)
    time.sleep(2)

    publish = driver.find_element(By.XPATH,f'(//span[text()="Publish"])[{publish_count}]')
    ActionChains(driver).move_to_element(publish).perform()
    time.sleep(3)

    publish.click()
    time.sleep(3)

    publish_final = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('settings','publish_final'))))
    publish_final.click()

    alert_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, get_config('settings','alert'))))
    alert_text = alert_element.text.strip()

    expected_message = "Policy status updated successfully"
    assert expected_message in alert_text

    print(alert_text)
    time.sleep(3)

    add_version_xpath = f"//span[text()='{policy_title_input}']//following::span[text()='Add Version'][1]"
    print(add_version_xpath)
    add_version_element = driver.find_element(By.XPATH, add_version_xpath)
    time.sleep(3)

    # Perform action using ActionChains to move to the element and click
    action = ActionChains(driver)
    action.move_to_element(add_version_element).click().perform()
    time.sleep(5)

    add_version = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,add_version_xpath)))
    add_version.click()
    time.sleep(2)

    add_version_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//button[@class='ant-btn css-w3qpxn ant-btn-default  app-btn-primary  '])")))
    add_version_button.click()
    time.sleep(5)


# def test_addVersion_invalid(driver,login):
#
#     add_version = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"(//span[text()='Add Version'])")))
#     final_add = len(add_version)
#     add = driver.find_element(By.XPATH,f"(//span[text()='Add Version'])[{final_add}]")
#     ActionChains(driver).move_to_element(add).perform()
#     time.sleep(3)
#     add.click()
#     version_down = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('settings','version_down'))))
#     version_down.click()
#     time.sleep(2)
#     alert_element = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, get_config('settings', 'alert_version_failed'))))
#     alert_text = alert_element.text.strip()
#
#     expected_message = "Version number cannot be below"
#     assert expected_message in alert_text
#     print("Assertion Successful")
#     time.sleep(5)
#
# def test_addVersion_valid(driver,login):
#
#     # version_up = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('settings','version_up'))))
#     # version_up.click()
#     # time.sleep(3)
#
#     version_decimal = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//input[@class='ant-input css-w3qpxn text-lg pl-5 '])[2]")))
#     time.sleep(2)
#     version=version_decimal.text.strip()
#     print(version)
#     print(type(version_decimal.text.strip()))
#
#     input_element = driver.find_element(By.XPATH,"(//input[@class='ant-input css-w3qpxn text-lg pl-5 '])[2]")
#
#     value = input_element.get_attribute('value')
#     print(type(value))
#
#     print("Value extracted from input:", value)
#     if value == "10":
#         # print("cannot update")
#         up = driver.find_element(By.XPATH,"(//span[@class='anticon anticon-up text-xs'])[1]")
#         up.click()
#         time.sleep(5)
#     add_version = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,get_config('settings','add_version'))))
#     add_version.click()
#     # alert_element = WebDriverWait(driver, 10).until(
#     #     EC.visibility_of_element_located((By.XPATH, get_config('settings', 'alert_version_success'))))
#     # alert_text = alert_element.text.strip()
#     #
#     # expected_message = "Version Created"
#     # assert expected_message in alert_text
#     # print("Assertion Successful")

# def test_addVersionPolicy(driver,login):
#     add_version = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"(//span[text()='Add Version'])")))
#     final_add = len(add_version)
#     time.sleep(3)
#     add = driver.find_element(By.XPATH,f"(//span[text()='Add Version'])[{final_add-1}]")
#     ActionChains(driver).move_to_element(add).perform()
#
#     add.click()
#     time.sleep(5)