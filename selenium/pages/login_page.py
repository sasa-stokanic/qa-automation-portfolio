from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    URL = "https://www.automationexercise.com/login"

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGGED_IN_TEXT = (By.XPATH, '//a[contains(text(),"Logged in as")]/b')
    LOGGED_IN_ASSERION = (By.CSS_SELECTOR, "i[class='fa fa-lock']")
    NOT_LOGGED_IN_TEXT = (By.XPATH, "//p[contains (text(), 'Your email or password is incorrect!')]")
    

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        self.driver.get(self.URL)
    
    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
    
    def get_logged_in_username(self):
         element = self.wait.until(EC.visibility_of_element_located(self.LOGGED_IN_TEXT))
         return element.text
    
    def is_login_confirmed(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOGGED_IN_ASSERION))
    
    def not_logged_in(self):
        return self.wait.until(EC.visibility_of_element_located(self.NOT_LOGGED_IN_TEXT))
    
    
