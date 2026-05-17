from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_cart_badge_and_cart_items_match_added_products(driver):

    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)

    items_to_add = 2
    expected_count = str(items_to_add)
    badge_locator = (By.CSS_SELECTOR, "[data-test=shopping-cart-badge]")


    wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=inventory-list]")))
    inventory_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item]")))

    for inventory_item in inventory_items[:items_to_add]:
        button = inventory_item.find_element(By.TAG_NAME,"button")
        wait.until(EC.element_to_be_clickable(button)).click()
    
    wait.until(EC.text_to_be_present_in_element(badge_locator,expected_count))

    cart_badge = driver.find_element(*badge_locator).text

    assert cart_badge == expected_count, "Cart badge does not match the expected count"

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=shopping-cart-link]"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=cart-list]")))
    cart_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,".cart_item")))

    assert len(cart_items) == items_to_add, "Number of cart items does not match the number of added items"



def test_cart_item_data_matches_inventory(driver):
    
    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)


    wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=inventory-list]")))
    inventory_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item]")))

    first_item = inventory_items[0]
    inventory_name = first_item.find_element(By.CSS_SELECTOR,"[data-test=inventory-item-name]").text
    inventory_price = float(
        first_item.find_element(By.CSS_SELECTOR,"[data-test=inventory-item-price]").text.replace("$",""))


    first_item.find_element(By.CSS_SELECTOR,"[data-test^=add-to-cart]").click()


    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[data-test=shopping-cart-badge]"),"1"))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=shopping-cart-link]"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=cart-contents-container]")))

    cart_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item]")))
    assert len(cart_items) == 1, "Expected 1 item in cart, but found different number"

    cart_item = cart_items[0]

    cart_name = cart_item.find_element(By.CSS_SELECTOR,"[data-test=inventory-item-name]").text
    cart_price = float(
        cart_item.find_element(By.CSS_SELECTOR,"[data-test=inventory-item-price]").text.replace("$",""))

    assert inventory_name == cart_name, "Product name in cart does not match inventory item"
    assert inventory_price == cart_price, "Product price in cart does not match inventory item price"


def test_remove_item_from_cart_page(driver):

    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)


    wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=inventory-list]")))

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=add-to-cart-sauce-labs-backpack]"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=add-to-cart-sauce-labs-onesie]"))).click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[data-test=shopping-cart-badge]"),"2"))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=shopping-cart-link]"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=cart-contents-container]")))
    cart_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item]")))
    assert len(cart_items) == 2, "Expected 2 items before removal"

    for item in cart_items:
        name = item.find_element(By.CSS_SELECTOR,"[data-test=inventory-item-name]").text
        if name == "Sauce Labs Backpack":
            item.find_element(By.CSS_SELECTOR,"[data-test^=remove]").click()
            break

    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[data-test=shopping-cart-badge]"),"1"))
    badge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=shopping-cart-badge]"))).text
    cart_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test=inventory-item]")))

    cart_names = []
    for item in cart_items:
        name = item.find_element(By.CSS_SELECTOR,"[data-test=inventory-item-name]").text
        cart_names.append(name)
    
    assert "Sauce Labs Backpack" not in cart_names, "Backpack should be removed from cart"
    assert "Sauce Labs Onesie" in cart_names, "Onesie should remain in cart"
    assert badge == "1", "Cart badge should update to 1 after item removal"


def test_remove_all_items_clears_cart_and_removes_badge(driver):

    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 10)

    items_to_add = 3


    wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test=inventory-list]")))
    item_list = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[data-test=inventory-item]")))
    
    for item in item_list[:items_to_add]:
        button = item.find_element(By.CSS_SELECTOR,"[data-test^=add-to-cart]")
        button.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test=shopping-cart-link]"))).click()
    cart_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,".cart_item")))
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".cart_item")) == items_to_add)

    for item in cart_items:
        button = item.find_element(By.CSS_SELECTOR,"[data-test^=remove]")
        button.click()

    
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR,".cart_item"))== 0)
    cart_items = driver.find_elements(By.CSS_SELECTOR,".cart_item")
    
    try: 
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"[data-test=shopping-cart-badge]")))
    except TimeoutException:
        assert False, "Cart badge is still visible after removing all items"

    assert len(cart_items) == 0, "Cart should be empty after removing all items"