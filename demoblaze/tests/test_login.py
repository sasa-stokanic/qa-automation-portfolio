from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_happy_path(driver):


    driver.get("https://www.demoblaze.com")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID,"login2"))).click()
    wait.until(EC.visibility_of_element_located((By.ID,"loginusername"))).send_keys("Stokanicsale")
    wait.until(EC.visibility_of_element_located((By.ID,"loginpassword"))).send_keys("12345")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in"]'))).click()
    welcome_text = wait.until(EC.visibility_of_element_located((By.ID,"nameofuser"))).text
    
    assert "Welcome" in welcome_text, "Login failed for valid user credentials"


def test_login_invalid_username(driver):


    driver.get("https://www.demoblaze.com")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID,"login2"))).click()
    wait.until(EC.visibility_of_element_located((By.ID,"loginusername"))).send_keys("Stokanicsalee")
    wait.until(EC.visibility_of_element_located((By.ID,"loginpassword"))).send_keys("1234567")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in"]'))).click()
    
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text

    assert "User does not exist." in alert_text, "Expected error alert for invalid username was not displayed"
    alert.accept()
    

