from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class HomePage(BasePage):
    _logo = (By.ID, 'logo')
    _input_search = (By.NAME, 'search')
    _button_search = (By.XPATH, "//div[@id='search']//button")
    _cart_total = (By.ID, 'cart-total')
    _currency = (By.XPATH,  "//*[@id='form-currency']//strong")
    _currency_dropdown = (By.XPATH, "//*[@id='form-currency']//button[@data-toggle]")
    _sin_coincidence = (By.XPATH, "//*[@id='content']/p[2]")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def is_logo_visible(self) -> bool:
        return self._get_element(self._logo).is_displayed()

    def search(self, text: str):
        self._write(self._input_search, text)
        self._click(self._button_search)

    def select_menu(self, menu_name: str):
        loc = (By.PARTIAL_LINK_TEXT, menu_name)
        self._click(loc)

    def select_sub_menu(self, main_menu_name: str, sub_menu_name: str):
        self.select_menu(main_menu_name)
        self.select_menu(sub_menu_name)

    def get_cart_total(self) -> str:        
        text = self._get_text(self._cart_total)
        #del texto 0 item(s) - $0.00 obtengo el precio; ej $0.00
        ''' 
        tex_price = text.split(' ') #lista 
        price = tex_price[3] en la pos 3 esta el valor
        '''
        return text
        

    def get_currency(self):
        currency = self._get_text(self._currency) 
        
        return currency

        

    def set_currency(self, name: str):
        ''' 
         Set currency.

        :param name: Valid options: EUR, GBP and USD.
        :return:None
        '''

        self._click(self._currency_dropdown)
        if name not in ['USD', 'GBP', 'EUR']:
            raise ValueError(f'Invalid currency: {name}')
        loc = (By.XPATH, f"//*[@id='form-currency']//button[@name='{name}']")
        self._click(loc)
   

    def select_product(self, name: str):
        loc = (By.PARTIAL_LINK_TEXT, name)
        #product : WebElement = self._wait_until_clickable(loc) ya se esta llamando en click
        self._click(loc)

    def get_product(self, name: str):
        loc = (By.PARTIAL_LINK_TEXT, name)
        return self._get_text(loc)

    def get_not_concidence(self):
        return self._get_text(self._sin_coincidence)

        