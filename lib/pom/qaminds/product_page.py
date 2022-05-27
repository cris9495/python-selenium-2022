from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class ProductPage(BasePage):
    #locators
    _name = (By.XPATH, '//h1')
    _price = (By.XPATH, "//div[@class='col-sm-4']//h2")
    _ex_tax = (By.XPATH, "//*[@class='col-sm-4']/ul[2]/li[2]")
    _pro_code = (By.XPATH,"//*[@class='col-sm-4']/ul[1]/li[1]")
    _availability = (By.XPATH,"//*[@class='col-sm-4']/ul[1]/li[2]")
    _descrip = (By.ID, "tab-description")
    _btn_cart = (By.ID, "button-cart")
    _total_review = (By.PARTIAL_LINK_TEXT, "reviews")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def get_name(self):
        return self._get_text(self._name)
        
    def get_price(self):
        return self._get_text(self._price)
        

    def get_ex_tax(self):
        return self._get_text(self._ex_tax)

    def get_product_code(self):
        return self._get_text(self._pro_code)

    def get_availability(self):
        return self._get_text(self._availability)

    def get_description(self):
        return self._get_text(self._descrip)

    def add_to_cart(self):
        self._click(self._btn_cart)

    def get_total_reviews(self):
        return self._get_text(self._total_review)
        



       