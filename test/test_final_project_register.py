from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.register_page import RegisterPage


class TestRegisterPage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()        
        self.register_page = RegisterPage(self.driver)
        self.register_page.goto("https://laboratorio.qaminds.com/index.php?route=account/register")
    
    def test_privacy(self):
        assert self.register_page.get_privacy() == "Privacy Policy", "Not text privacy"

    def test_advertise_email(self):
        self.register_page.set_email('azul')
        self.register_page.opc_continue()             
        assert self.register_page.get_email_validation() == """Please include an '@' in the email address. 'azul' is missing an '@'."""

    def teardown_method(self):
        if self.driver:
            self.driver.quit()   