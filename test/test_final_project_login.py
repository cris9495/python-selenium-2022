from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.login_page import LoginPage


class TestLoginPage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()        
        self.login_page = LoginPage(self.driver)
        self.login_page.goto("https://laboratorio.qaminds.com/index.php?route=account/login")
    
    def test_forgot_password(self):
        self.login_page.forgotten_password()
        

    def test_loging_incorrect(self):
        self.login_page.login('casa@yop.co','se0')
        assert self.login_page.is_login_warn_displayed(),"Warn should be displayed"
        

    def test_address_book(self):
        self.login_page.select_menu('Address Book')
        

    def test_login_register(self):
        self.login_page.select_menu('Register')
        
    
    def teardown_method(self):
        if self.driver:
            self.driver.quit()