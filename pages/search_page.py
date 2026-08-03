from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SearchPage:

    URL = "https://www.automationexercise.com/products"
    SEARCH_DRESS_URL = "https://www.automationexercise.com/products?search=dress"
    EMPTY_SEARCH_URL = "https://www.automationexercise.com/products?search="
    MOTOR_BIKE_URL = "https://www.automationexercise.com/products?search=MotorBike"
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    PRODUCTS = (By.CSS_SELECTOR, ".single-products")
    

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        self.driver.get(self.URL)
    
    def search_input(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT)).send_keys("dress")

    def empty_search_input(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT)).send_keys("")
    
    def search_button_click(self):
        button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
    
    def get_products(self, wait_for_results=True):  
        if wait_for_results:                        
            return self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCTS))  
        else:
            return self.driver.find_elements(*self.PRODUCTS)
    
    def wait_for_url(self):
        return self.wait.until(EC.url_contains("search"))
    
    def non_existing_product_search(self):
        return self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT)).send_keys("MotorBike")
    
    