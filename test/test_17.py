from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.login_page import LoginPage


class TestLoginPage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.login_page = LoginPage(self.driver)
        self.login_page.goto("https://laboratorio.qaminds.com/index.php?route=account/login")
        
        #self.driver.get("https://laboratorio.qaminds.com/index.php?route=account/login")
        

    def test_invalid_login(self):        
        self.login_page.login('ophj',123)
        assert self.login_page.is_login_warn_displayed(),"Warn should be displayed"

    def test_forgotten_password(self):
        self.login_page.forgotten_password()
        
    def test_continue_as_new_customer(self):
        self.login_page.continue_as_new_customer()

    def test_select_menu(self):
        self.login_page.select_menu("Login")
        self.login_page.select_menu("Register")
        self.login_page.select_menu("My Account")
        self.login_page.select_menu("Address Book")

       
        
    



    def teardown_method(self):
        if self.driver:
            self.driver.quit()