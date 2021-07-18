from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from time import sleep

driver = webdriver.Firefox()
driver.get("https://auth.uber.com/login/?breeze_local_zone=dca1&next_url=https%3A%2F%2Fm.uber.com%2F%3Fuclick_id%3D6db58b11-59e5-4b63-b64e-00de7d0e0e04&state=Dp6iqEL9JlSX5h-p8K6LcCb5wElGfILD7eq8pJyL3kM%3D")

campoNum = driver.find_element_by_name("phoneNumber")
campoNum.send_keys('27988125213')
campoNum.send_keys(Keys.ENTER)

try:
    codCel = str(input('Insira o código de celular >>'))
    driver.find_element_by_xpath('//*[@id="smsOTP"]').send_keys(codCel)
    driver.find_element_by_xpath('//*[@id="smsOTP"]').send_keys(Keys.ENTER)
except:
    pass

sleep(10)
driver.find_element_by_xpath('//*[@id="password"]').send_keys('7412369')
driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)

sleep(10)
driver.get("https://riders.uber.com/trips")
r = requests.get(driver.get("https://riders.uber.com/trips"))
print(r.text)