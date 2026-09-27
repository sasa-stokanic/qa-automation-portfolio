from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class RegisterPage:
    URL = "https://www.automationexercise.com/login"

    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SINGUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    REDIRECT_ENTER_ACCOUNT_INFO = (By.ID, "form")
    NAME_REGISTER_INPUT = (By.ID, "name")
    PASSWORD_REGISTER_INPUT = (By.ID, "password")
    BIRTH_DAY = (By.ID, "days")
    MONTH_DAY = (By.ID, "months")
    BIRTH_YEAR = (By.ID, "years")
    GENDER_MR = (By.ID, "uniform-id_gender1")
    GENDER_MRS = (By.ID, "uniform-id_gender2")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS = (By.ID, "address1")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED = (By.CSS_SELECTOR, "[data-qa='account-created']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-qa='continue-button']")
    DELETE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/delete_account']")
    ACCOUNT_DELETED_CONFIRMATION = (By.CSS_SELECTOR, "[data-qa='account-deleted']")
    EMAIL_ALREADY_EXIST = (By.XPATH, "//p[contains (text(), 'Email Address already exist!')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
    
    def register(self, name, email):
        self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(self.SINGUP_BUTTON)).click()

    def enter_account_info(self):
        return self.wait.until(EC.visibility_of_element_located(self.REDIRECT_ENTER_ACCOUNT_INFO))
    
    def select_gender(self):
        self.wait.until(EC.element_to_be_clickable(self.GENDER_MR)).click()

    def enter_name_password(self, name, password):
        self.wait.until(EC.visibility_of_element_located(self.NAME_REGISTER_INPUT)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_REGISTER_INPUT)).send_keys(password)

    def select_birth_day(self, day, month, year):
        Select(self.driver.find_element(*self.BIRTH_DAY)).select_by_visible_text(day)
        Select(self.driver.find_element(*self.MONTH_DAY)).select_by_visible_text(month)
        Select(self.driver.find_element(*self.BIRTH_YEAR)).select_by_visible_text(year)
    
    def enter_user_info(self,name,lastName,address,state,city,zipcode,mobile):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(lastName)
        self.wait.until(EC.visibility_of_element_located(self.ADDRESS)).send_keys(address)
        self.wait.until(EC.visibility_of_element_located(self.STATE)).send_keys(state)
        self.wait.until(EC.visibility_of_element_located(self.CITY)).send_keys(city)
        self.wait.until(EC.visibility_of_element_located(self.ZIPCODE)).send_keys(zipcode)
        self.wait.until(EC.visibility_of_element_located(self.MOBILE_NUMBER)).send_keys(mobile)
    
    def create_account(self):
        button = self.wait.until(EC.presence_of_element_located(self.CREATE_ACCOUNT_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)

    def account_created(self):
        return self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_CREATED))

    
    def continue_button(self):
        button = self.wait.until(EC.presence_of_element_located(self.CONTINUE_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)
    
    def delete_account(self):
        button = self.wait.until(EC.presence_of_element_located(self.DELETE_ACCOUNT_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)

    def account_deleted(self):
        return self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_DELETED_CONFIRMATION))
    
    def sign_up_existing_email(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMAIL_ALREADY_EXIST))

