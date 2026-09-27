from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class CheckoutPage:

    LOGIN_URL = "https://www.automationexercise.com/login"
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGGED_IN_TEXT = (By.XPATH, '//a[contains(text(),"Logged in as")]/b')
    VIEW_PRODUCT = (By.CSS_SELECTOR, "a[href^='/product_details/1']")
    ADD_TO_CART_PRODUCT = (By.CSS_SELECTOR, ".btn-default.cart")
    VIEW_CART = (By.CSS_SELECTOR, "a[href='/view_cart']")
    CART_PRODUCTS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    LOGGED_IN_ASSERION = (By.CSS_SELECTOR, "i[class='fa fa-lock']")
    PRODUCT_PAGE_BUTTON = (By.CSS_SELECTOR, "a[href^='/products']")
    ADD_CLOSE_CLICK = (By.ID, "dismiss-button-element")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn-default.check_out")
    PRODUCT_NAME = (By.CSS_SELECTOR, "td.cart_description a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "td.cart_total p")
    PRODUCT_NAME_CHECKOUT = (By.CSS_SELECTOR, "td.cart_description a")
    PRODUCT_PRICE_CHECKOUT = (By.CSS_SELECTOR, "td.cart_total p")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver , 10)
    
    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)
    
    def login(self,email,password):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
    
    def login_confirmation(self):
        element = self.wait.until(EC.visibility_of_element_located(self.LOGGED_IN_TEXT))
        return element.text
    
    def close_add_if_present(self):
        try:
            shot_wait = WebDriverWait(self.driver, 5)
            add_close_button = shot_wait.until(EC.element_to_be_clickable(self.ADD_CLOSE_CLICK))
            add_close_button.click()
        except TimeoutException:
            pass
    
    def open_product_page(self):
        element = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_PAGE_BUTTON))
        self.driver.execute_script("arguments[0].click();", element)
    
    def open_view_product(self):
        element = self.wait.until(EC.element_to_be_clickable(self.VIEW_PRODUCT))
        self.driver.execute_script("arguments[0].click();", element)

    def add_to_cart_in_product_view(self):
        #self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_PRODUCT)).click()
        button = self.wait.until(EC.presence_of_element_located(self.ADD_TO_CART_PRODUCT))
        self.driver.execute_script("arguments[0].click();", button)

    def view_cart(self):
        link = self.wait.until(EC.presence_of_element_located(self.VIEW_CART))
        self.driver.execute_script("arguments[0].click();", link)
        self.wait.until(EC.url_contains("view_cart"))
    
    def product_in_cart_confirmation(self):
        products = self.wait.until(EC.visibility_of_all_elements_located(self.CART_PRODUCTS))
        return len(products)
    
    def take_product_name_in_cart(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME)).text
    
    def take_product_price_in_cart(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE)).text
    
    def checkout_button_click(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    def take_product_name_in_checkout(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME_CHECKOUT)).text
    
    def take_product_price_in_checkout(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE_CHECKOUT)).text
    
    