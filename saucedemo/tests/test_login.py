from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_happy_path(driver):
    
    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=username]"))).send_keys("standard_user")
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=password]"))).send_keys("secret_sauce")
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=login-button]"))).click()

    inventory_container = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,'[data-test="inventory-container"]')))

    assert inventory_container, "Inventory container is not visible after login"



def test_login_invalid_password(driver):

    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=username]"))).send_keys("standard_user")
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=password]"))).send_keys("invalid_password")
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=login-button]"))).click()

    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[data-test="error"]')))

    assert error_message, "Error message is not visible after login with invalid password"
    assert "do not match" in error_message.text, "Expected error message not found"