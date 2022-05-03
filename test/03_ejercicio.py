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
my_account: WebElement = driver.find_element(By.LINK_TEXT, "My Account")
assert my_account.is_displayed(), "my account is not visible"
my_account.click()

opc_login: WebElement = driver.find_element(By.LINK_TEXT, "Login")
assert opc_login.is_displayed(), "login is not visible"
opc_login.click()

correo : WebElement = driver.find_element(By.NAME, "email")
assert correo.is_displayed(), "correo is not visible"
correo.clear()
correo.send_keys("casa")

login_btn = WebElement = driver.find_element(By.XPATH, '//input[@value="Login"]')
assert login_btn.is_displayed(), "login is not visible"
login_btn.click()

clase_error : WebElement = driver.find_element(By.XPATH, "alert alert-danger alert-dismissible")
assert clase_error.is_displayed(),"no hay error"

clase_error.text == " Warning: No match for E-Mail Address and/or Password.", "no coincide el texto de error"





# Close browser
#driver.quit()