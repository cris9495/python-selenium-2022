from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class LoginPage(BasePage):
    #locators
    _email = (By.ID, 'input-email')
    _password = (By.ID, 'input-password')
    _btn_login = (By.XPATH, "//input[@value='Login']")
    _forgot_password = (By.LINK_TEXT,"Forgotten Password")
    _continue = (By.LINK_TEXT,"Continue")
    _alert = (By.CLASS_NAME, "alert-danger")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def login(self, user, password):
        self._write(self._email,user)
        self._write(self._password, password)
        self._click(self._btn_login)

        

    def forgotten_password(self):
        self._click(self._forgot_password)

        

    def select_menu(self, name: str):
        loc = (By.LINK_TEXT, name)
        self._click(loc)

        

    def continue_as_new_customer(self):
        self._click(self._continue)

    def is_login_warn_displayed(self):
        return self._get_element(self._alert).is_displayed()

        