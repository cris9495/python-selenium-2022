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
        """Ejercicio 15"""
        # Open web page
        self.driver.get("https://laboratorio.qaminds.com/")

        # icon $
        loc_1 = (By.XPATH, "//*[@class='btn btn-link dropdown-toggle']/strong")
        text_signo = self.wait.until(EC.text_to_be_present_in_element(loc_1,"$"))
        

        #select input search
        search_input = (By.XPATH, '//*[@id="search"]/input')
        search_inp : WebElement = self.wait.until(EC.presence_of_element_located(search_input))        
        search_inp.clear()
        search_inp.send_keys("Samsung")
        
        btn_search = (By.XPATH, '//*[@id="search"]/span/button')
        btn : WebElement = self.wait.until(EC.element_to_be_clickable(btn_search))
        btn.click()

        #select samsung syncmastesr
        loc = (By.LINK_TEXT, "Samsung SyncMaster 941BW")
        btn_desk : WebElement = self.wait.until(EC.element_to_be_clickable(loc))
        btn_desk.click()

        #Price usd
        loc_price = (By.XPATH, "//*[@class='list-unstyled']//h2")
        number_1 : WebElement = self.wait.until(EC.visibility_of_element_located(loc_price))
        price_usd = number_1.text   #dado el xpath guardo el texto visualizado
        price_usd = float(price_usd[1:])

        #select el dropdown de Currency
        dropdown_loc = (By.XPATH, "//*[@id='form-currency']//button[@data-toggle='dropdown']")
        dropdown : WebElement = self.wait.until(EC.element_to_be_clickable(dropdown_loc))
        dropdown.click()

        #select euros
        eur_loc = (By.NAME,"EUR")
        opc_eur : WebElement = self.wait.until(EC.element_to_be_clickable(eur_loc))
        opc_eur.click()

        price_eu : WebElement = self.wait.until(EC.visibility_of_element_located(loc_price))
        price_eur = price_eu.text
        price_eur = float(price_eur[:-1])

        assert price_eur < price_usd
    
        #print(price_usd)
    

    def teardown_method(self):
        if self.driver:
            self.driver.quit()
