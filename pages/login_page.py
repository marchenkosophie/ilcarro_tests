import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    LOGIN_NAV_LINK = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    YALLA_BUTTON = (By.XPATH, "//button[text()='Y’alla!']")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, "h3")
    OK_BTN = (By.XPATH, "//*[text()='OK']")
    SIGN_OUT_BTN = (By.XPATH, "//*[text()='Log out']")
    LOGIN_FAILED = (By.XPATH, "//*[text()='\"Login or Password incorrect\"']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")


    def __init__(self, driver):
        self.driver = driver


    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()
        time.sleep(2)


    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)



    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)



    def submit_login(self):
        self.driver.find_element(*self.YALLA_BUTTON).click()


    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()

    def login_success_text(self):
        # return self.driver.find_element(*self.CONFIRMATION_TEXT).text
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONFIRMATION_TEXT))
        return element.text


    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()

    def is_logged(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.SIGN_OUT_BTN)
            )
            return True
        except TimeoutException:
            return False


    def is_not_logged(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.LOGIN_FAILED)
            )
            return True
        except TimeoutException:
            return False


    def is_submit_button_enabled(self):
        return self.driver.find_element(*self.YALLA_BUTTON).is_enabled()


    def error_message_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return element.text


