from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage


class TestHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.home_page = HomePage(self.driver)

    def test_text_samsung(self):
        self.home_page.search("Samsung")        
        assert self.home_page.get_product("Samsung SyncMaster") == "Samsung SyncMaster 941BW"

    def test_SinCoincidencia(self):
        self.home_page.search("aa")
        assert self.home_page.get_not_concidence() == "There is no product that matches the search criteria."

        