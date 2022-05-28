from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage


class TestHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.home_page = HomePage(self.driver)

    def test_currency_pesos(self):
        assert self.home_page.get_currency() == "$", "currency is not in pesos"

    def test_currency_euro(self):
        self.home_page.set_currency("EUR")
        assert "€" == self.home_page.get_currency(), "there was not selected currency euro"

    def test_currency_pound(self):
        self.home_page.set_currency("GBP")
        assert "£" == self.home_page.get_currency(), "there was not selected currency Pound Sterling"
      
    def teardown_method(self):
        if self.driver:
            self.driver.quit()    
        

