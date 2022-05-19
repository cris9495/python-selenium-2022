import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Init Browsers
from selenium.webdriver.remote.webelement import WebElement

chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'

url = 'https://wasi.co/login-usuario.htm'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

driver.get(url)
time.sleep(5)

campo_correo: WebElement = driver.find_element(By.ID, "user")
assert campo_correo.is_displayed(), "No esta el campo"
campo_correo.clear()
campo_correo.send_keys('pr@yop.co')

time.sleep(5)
campo_pass : WebElement = driver.find_element(By.ID, "password")
assert campo_pass.is_displayed(), "No esta el campo"
campo_pass.clear()
campo_pass.send_keys('this')

btn: WebElement = driver.find_element(By.ID, "login")
assert btn.is_displayed(), "Button login is not visible"
btn.click()

text_error : WebElement = driver.find_element(By.XPATH, "//body//div[@class='alerts-inf alert alert-danger']")
assert text_error.is_displayed(), "there is not error"
assert text_error.text == "Correo o contraseña incorrecta","no coincide"