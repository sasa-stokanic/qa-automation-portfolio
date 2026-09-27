from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class CartPage:

    URL = "https://www.automationexercise.com/products"
    VIEW_PRODUCT = (By.CSS_SELECTOR, "a[href^='/product_details/1']")
    ADD_TO_CART_PRODUCT1 = (By.CSS_SELECTOR, ".btn.btn-default.cart")
    NAVIGATE_TO_CART = (By.CSS_SELECTOR, "a[href^='/view_cart']")
    VIEW_CART = (By.CSS_SELECTOR, ".text-center a")
    CONFIRMATION =  (By.XPATH,"//p[contains (text(), 'Your product has been added to cart.')]")
    PRODUCT_NAME_CART = (By.CSS_SELECTOR, "td.cart_description a")
    CART_DELETE_BUTTON = (By.CSS_SELECTOR, "td.cart_delete a")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "p.text-center b")
    ADD_TO_CART_OVERLAY_BUTTON = (By.CSS_SELECTOR, ".product-overlay a.add-to-cart")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, ".close-modal")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".single-products")
    CART_PRODUCTS = (By.CSS_SELECTOR, "tbody tr")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-information span span")
    QUANTITY_INPUT = (By.ID, "quantity")
    CART_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity")
    CART_PRODUCT_PRICE = (By.CSS_SELECTOR, ".cart_total p")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_products_page(self):
        self.driver.get(self.URL)

    def view_product(self):
        element = self.wait.until(EC.element_to_be_clickable(self.VIEW_PRODUCT))
        self.driver.execute_script("arguments[0].click();", element)

    def add_to_cart(self):

        element = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_PRODUCT1))
        self.driver.execute_script("arguments[0].click();", element)

    def product_is_added(self):
        return self.wait.until(EC.visibility_of_element_located(self.CONFIRMATION)) 
    
    def view_cart_from_page(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        return self.wait.until(EC.element_to_be_clickable(self.NAVIGATE_TO_CART)).click()

    def view_cart(self):
        return self.wait.until(EC.element_to_be_clickable(self.VIEW_CART)).click()
    
    def get_cart_item_names(self):
        rows = self.wait.until(EC.visibility_of_all_elements_located(self.CART_PRODUCTS))
        return [row.find_element(By.CSS_SELECTOR, "td.cart_description a").text.strip() for row in rows]
    
    def product_name_in_cart(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME_CART)).text

    def remove_item_from_cart(self):
        return self.wait.until(EC.element_to_be_clickable(self.CART_DELETE_BUTTON)).click()
    
    def get_empty_cart_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART_MESSAGE)).text
    
    def continue_shopping(self):
        return self.wait.until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)).click()
    
    def hover_over_product(self, index):
        products = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARDS))
        ActionChains(self.driver).move_to_element(products[index]).perform()
    
    def add_multiple_products_to_cart(self, indices):
        for index in indices:
            self.hover_over_product(index)
            buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_OVERLAY_BUTTON))
            self.driver.execute_script("arguments[0].click();", buttons[index])
            self.continue_shopping()

    def get_cart_items_count(self):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.CART_PRODUCTS))
        return len(items)
    

    def add_product_to_cart_via_user_click(self, index):
        products = self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCT_CARDS))
        product = products[index]
    
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
        ActionChains(self.driver).move_to_element(product).perform()
    
        overlay_button = self.wait.until(EC.visibility_of(product.find_element(*self.ADD_TO_CART_OVERLAY_BUTTON)))
        overlay_button.click()  # PRAVI klik, ne JS
        self.continue_shopping()

    
    def product_price_in_view_product(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE))
    
    def cart_product_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_PRODUCT_PRICE))
    
    def set_quantity(self, quantity):
        quantity_input = self.wait.until(EC.visibility_of_element_located(self.QUANTITY_INPUT))
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))
    
    def cart_quantity(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_QUANTITY)).text

        
