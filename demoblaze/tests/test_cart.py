from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart(driver):

    wait = WebDriverWait(driver, 10)
    driver.get("https://www.demoblaze.com")
    

    wait.until(EC.element_to_be_clickable((By.XPATH,'//a[contains(text(),"Samsung galaxy s6")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Add to cart")]'))).click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    wait.until(EC.element_to_be_clickable((By.ID,"cartur"))).click()
    cart_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"#tbodyid tr")))

    assert len(cart_items) == 1, "Cart should contain 1 item after adding product"



def test_remove_from_cart(driver):

    wait = WebDriverWait(driver, 10)
    driver.get("https://www.demoblaze.com")


    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Samsung galaxy s6")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Add to cart")]'))).click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    wait.until(EC.element_to_be_clickable((By.ID,"cartur"))).click()
    wait.until(EC.url_contains("cart.html"))
    cart_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"#tbodyid tr")))
    assert len(cart_items) == 1, "Added product was not displayed in the cart"

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#tbodyid tr td a"))).click()
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR,"#tbodyid tr")) == 0)
    cart_items = driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")

    assert len(cart_items) == 0, "Product was not removed from the cart"



def test_cart_item_matches_selected_product(driver):

    wait = WebDriverWait(driver, 10)
    driver.get("https://www.demoblaze.com")


    product = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Samsung galaxy s6')]")))
    product_name = product.text
    product.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Add to cart")]'))).click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    wait.until(EC.element_to_be_clickable((By.ID,"cartur"))).click()

    cart_name = wait.until(
    EC.visibility_of_element_located((By.XPATH, f"//td[contains(text(),'{product_name}')]"))).text

    assert product_name == cart_name, "Added product does not match product displayed in cart"




def test_cart_persistence_after_refresh(driver):

    wait = WebDriverWait(driver, 10)
    driver.get("https://www.demoblaze.com")


    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Samsung galaxy s6")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Add to cart")]'))).click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    wait.until(EC.element_to_be_clickable((By.ID,"cartur"))).click()
    wait.until(EC.url_contains("cart.html"))
    cart_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"#tbodyid tr")))

    assert len(cart_items) == 1, "Added product was not displayed in the cart before refresh"

    driver.refresh()

    wait.until(EC.url_contains("cart.html"))

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR,"#tbodyid tr"))== 1)
    cart_items = driver.find_elements(By.CSS_SELECTOR,"#tbodyid tr")
    product_name_after = driver.find_element(By.CSS_SELECTOR,"#tbodyid tr td:nth-child(2)").text
    
    assert len(cart_items) == 1, "Cart item was not preserved after page refresh"
    assert product_name_after == "Samsung galaxy s6", "Incorrect product was displayed after page refresh"