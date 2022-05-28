from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.product_page import ProductPage


class TestProductPage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.product_page = ProductPage(self.driver)
        self.product_page.goto("https://laboratorio.qaminds.com/index.php?route=product/product&product_id=33&search=samsung")

    def test_get_precio(self):      
        assert self.product_page.get_price()[1:] == "242.00", "el precio de productor no es 242.00"
      

    def test_get_availability(self):
        assert self.product_page.get_availability()[14:] == "In Stock", "the availa no esta en stock"

    

