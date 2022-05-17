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
        """Ejercicio 13"""
        # Open web page
        self.driver.get("https://laboratorio.qaminds.com/")

        # input word
        search_input = (By.XPATH, '//*[@id="search"]/input')
        search_inp : WebElement = self.wait.until(EC.presence_of_element_located(search_input))        
        search_inp.clear()
        search_inp.send_keys("Display")

         
        btn_search = (By.XPATH, '//*[@id="search"]/span/button')
        btn : WebElement = self.wait.until(EC.element_to_be_clickable(btn_search))
        btn.click()

        #text there is not products
        content = (By.XPATH, '//*[@id="content"]/p[2]')
        text : WebElement = self.wait.until(EC.presence_of_element_located(content))
        assert text.text == 'There is no product that matches the search criteria.', 'Text does not exist'

        #select check Search in products
        chec = (By.XPATH, '//*[@id="description"]')
        my_chec : WebElement = self.wait.until(EC.presence_of_element_located(chec))
        my_chec.click()

        btn_search = (By.XPATH, '//*[@id="button-search"]')
        btn : WebElement = self.wait.until(EC.element_to_be_clickable(btn_search))
        btn.click()

        products = ['Apple Cinema 30"', 'iPod Nano', 'iPod Touch', 'MacBook Pro']

        for product_name in products:
            loc = (By.LINK_TEXT, product_name)
            self.wait.until(EC.element_to_be_clickable(loc))
        ''' 
        apple_c = (By.LINK_TEXT, 'Apple Cinema 30"')
        apple_ci : WebElement = self.wait.until(EC.presence_of_element_located(apple_c))
        assert apple_c, 'no esta el apple cinema'
        '''


        



        
    
''' 
    def teardown_method(self):
        if self.driver:
            self.driver.quit()
'''