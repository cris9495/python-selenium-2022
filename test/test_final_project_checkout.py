from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.checkout_page import CheckPage


class TestCheckPage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.checkout_page = CheckPage(self.driver)
        self.checkout_page.goto("https://laboratorio.qaminds.com/index.php?route=product/product&product_id=33&search=samsung")
        self.checkout_page.add_to_cart()
        self.checkout_page.check_select()

    def test_forgot_pass(self):  
        self.checkout_page.forget_pass()    

    def test_guest_checkout(self):
        self.checkout_page.radio_g_check()
        
   
      