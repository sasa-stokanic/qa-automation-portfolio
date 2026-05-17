from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


def test_products_are_sorted_by_price_low_to_high(driver):

    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)


    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test=inventory-container]")))

    prices = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item-price]")))
    prices_before = []
    for p in prices:
        price_value = float(p.text.replace("$",""))
        prices_before.append(price_value)
    
    sort = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=product-sort-container]")))
    Select(sort).select_by_visible_text("Price (low to high)")

    def waiting_sort(d):

        prices = d.find_elements(By.CSS_SELECTOR,"[data-test=inventory-item-price]")
        new_prices = []
        for p in prices:
            price_value = float(p.text.replace("$",""))
            new_prices.append(price_value)
        
        return prices_before != new_prices
    wait.until(waiting_sort)
    
    sorted_items = []
    post_sort = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item-price]")))
    for ps in post_sort:
        price_value = float(ps.text.replace("$",""))
        sorted_items.append(price_value)
    
    assert prices_before != sorted_items, "Product order did not change after applying low to high sorting"

    for i in range(len(sorted_items)-1):
        assert sorted_items[i] <= sorted_items[i + 1], "Products are not sorted correctly from low to high price"