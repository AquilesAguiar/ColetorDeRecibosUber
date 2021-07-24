from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Firefox()
driver.get("https://auth.uber.com/login/session")
email = driver.find_element_by_id("useridInput")
email.send_keys("aquilesvibe@hotmail.com")
email.send_keys(Keys.ENTER)
sleep(10)
driver.find_element_by_id('password').send_keys('7412369')
driver.find_element_by_id('password').send_keys(Keys.ENTER)


sleep(10)
driver.get("https://riders.uber.com/trips")
# html = requests.get(driver.current_url)
# print(html.text)
r = BeautifulSoup(driver.page_source, 'html.parser')
print(r.prettify())
with open('pagina.txt','w') as pagina:
    pagina.write(str(r.prettify()))