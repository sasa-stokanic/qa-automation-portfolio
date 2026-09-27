from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage:

    URL = "https://www.automationexercise.com/products"
    VIEW_PRODUCT = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    ADD_TO_CART_PRODUCT1 = (By.CSS_SELECTOR, ".btn.btn-default.cart")
    CONFIRMATION =  (By.XPATH,"//p[contains (text(), 'Your product has been added to cart.')]")
    VIEW_CART = (By.CSS_SELECTOR, "#cartModal a[href='/view_cart']")
    PRODUCT_NAME_CART = (By.CSS_SELECTOR, "td.cart_description a")
    PRODUCT_NAME_IN_VIEW = (By.CSS_SELECTOR, ".product-information h2")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-information span span")

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
    
    def product_name_in_view_product(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME_IN_VIEW))
    
    def product_price_in_view_product(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE))
    
    def view_product_by_index(self, index):
        products = self.wait.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "a[href^='/product_details/']")
    ))
        element = products[index]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
         
    