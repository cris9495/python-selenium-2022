from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestDownload:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())

    def test_download_button_1(self):
        """Ejercicio 14"""
        # Open web page
        self.driver.get("https://laboratorio.qaminds.com/")

        # select option Desktop
        loc = (By.LINK_TEXT, "Desktops")
        btn_desk : WebElement = self.wait.until(EC.element_to_be_clickable(loc))
        btn_desk.click()

        #select mac
        loc = (By.PARTIAL_LINK_TEXT, "Mac")
        opc_mac : WebElement = self.wait.until(EC.element_to_be_clickable(loc))
        opc_mac.click()

        #Text imac
        loc = (By.PARTIAL_LINK_TEXT, "iMac")
        texti = self.wait.until(EC.text_to_be_present_in_element(loc,"iMac"))

        #select imac
        opc_iMac : WebElement = self.wait.until(EC.presence_of_element_located(loc))
        opc_iMac.click()

        #select add to Cart
        loc = (By.XPATH, "//*[@class='btn btn-primary btn-lg btn-block']")
        btn_add : WebElement = self.wait.until(EC.element_to_be_clickable(loc))
        btn_add.click()

        #Watch on bottun text item..
        loc = (By.XPATH, "//*[@id='cart-total']")
        text_item = self.wait.until(EC.text_to_be_present_in_element(loc,"1 item(s) - $122.00"))
        
    
''' 
    def teardown_method(self):
        if self.driver:
            self.driver.quit()
'''