import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Init Browsers
from selenium.webdriver.remote.webelement import WebElement

chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://qamindslab.com'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open Web Page
driver.get("https://laboratorio.qaminds.com/")
time.sleep(5)

# Test Logic
laptop : WebElement = driver.find_element(By.LINK_TEXT, "Laptops & Notebooks")
assert laptop.is_displayed(), "no hay opcion lapton"
laptop.click()

opc_win : WebElement = driver.find_element(By.LINK_TEXT, "Windows (0)")
assert opc_win.is_displayed(), "windows is not visible"
opc_win.click()

textoS : WebElement = driver.find_element(By.NAME, "There are no products to list in this category.")
assert textoS.is_displayed(), "texto is not visible"







# Close browser
#driver.quit()