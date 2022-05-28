from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class RegisterPage(BasePage):
    #locators
    _email = (By.ID, 'input-email')
    _password = (By.ID, 'input-password')
    _opc_privacy = (By.XPATH, "//*[@class='agree']")
    _modal_privacy = (By.XPATH, "//*[@class='modal-title']")  #(By.LINK_TEXT,"Forgotten Password")
    _continue = (By.XPATH,"//*[@value='Continue']")
    _alert = (By.CLASS_NAME, "alert-danger")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def login(self, user, password):
        self._write(self._email,user)
        self._write(self._password, password)
        self._click(self._btn_login)

    def get_privacy(self):
        self._click(self._opc_privacy)
        return self._get_text(self._modal_privacy)

    def set_email(self, correo):
        self._write(self._email, correo)

    def opc_continue(self):
        self._click(self._continue)

    def get_email_validation(self):
        email_camp = self._get_element(self._email)
        return email_camp.get_attribute('validationMessage')
       
