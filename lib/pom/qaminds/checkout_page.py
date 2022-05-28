from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class CheckPage(BasePage):
    #locators
    
    _btn_cart = (By.ID, "button-cart")
    _opc_checkout = (By.PARTIAL_LINK_TEXT, "Checkout")
    _opc_forgot = (By.PARTIAL_LINK_TEXT, "Forgotten Password")
    _radio_guest = (By.XPATH, "//*[@value='guest']")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)
    

    def add_to_cart(self):
        self._click(self._btn_cart)

    def check_select(self):
        self._click(self._opc_checkout)

    def forget_pass(self):
        self._click(self._opc_forgot)

    def radio_g_check(self):
        self._click(self._radio_guest)