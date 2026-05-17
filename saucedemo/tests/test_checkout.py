from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def test_checkout_shows_error_when_required_fields_are_empty(driver):

    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)


    wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=inventory-container]")))

    items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test^=add-to-cart]")))
    items[0].click()

    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[data-test=shopping-cart-badge]"),"1"))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=shopping-cart-link]"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=checkout]"))).click()


    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=continue]"))).click()
    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=error]")))

    assert error_message.is_displayed(), "Error message was not displayed after submitting empty checkout form"
    assert "Error" in error_message.text, "Error message text did not contain expected validation message"


def test_checkout_overview_displays_correct_item_and_subtotal(driver):

    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)


    wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=inventory-container]")))

    inventory_item = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item]")))
    first_item = inventory_item[0]
    second_item = inventory_item[1]

    first_price = float(
        first_item.find_element(By.CSS_SELECTOR,"[data-test=inventory-item-price]").text.replace("$",""))
    second_price = float(
        second_item.find_element(By.CSS_SELECTOR,"[data-test=inventory-item-price]").text.replace("$",""))
    
    expected_subtotal = round (first_price + second_price, 2)

    first_item.find_element(By.CSS_SELECTOR,"[data-test^=add-to-cart]").click()
    second_item.find_element(By.CSS_SELECTOR,"[data-test^=add-to-cart]").click()
    

    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[data-test=shopping-cart-badge]"),"2"))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=shopping-cart-link]"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=checkout]"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=firstName]"))).send_keys("User")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=lastName]"))).send_keys("Tester")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=postalCode]"))).send_keys("11000")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=continue]"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=checkout-summary-container]")))

    overview_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item]")))
    actual_subtotal_text = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=subtotal-label]"))).text
    actual_subtotal = float(actual_subtotal_text.replace("Item total: $",""))
    
    
    assert len(overview_items) == 2, "Checkout overview should display 2 selected items"
    assert actual_subtotal == expected_subtotal, "Checkout subtotal does not match selected item prices"


def test_user_can_complete_order_successfully(driver):

    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)


    wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=inventory-container]")))

    inventory_item = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item]")))
    first_item = inventory_item[0]

    first_item.find_element(By.CSS_SELECTOR,"[data-test^=add-to-cart]").click()


    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[data-test=shopping-cart-badge]"),"1"))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=shopping-cart-link]"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=checkout]"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=firstName]"))).send_keys("User")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=lastName]"))).send_keys("Tester")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=postalCode]"))).send_keys("11000")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=continue]"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=checkout-summary-container]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=finish]"))).click()
    confirmation_container = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=checkout-complete-container]")))
    
    assert confirmation_container.is_displayed(), "Order confirmation page was not displayed after checkout"