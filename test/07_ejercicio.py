from xml.sax.xmlreader import Locator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)


locator = (By.ID,"at-cv-lightbox-close" )
search_btn : WebElement = wait.until(EC.visibility_of_element_located(locator))
assert search_btn.is_enabled(), "pop close button is not enabled"
search_btn.click()

driver.quit()