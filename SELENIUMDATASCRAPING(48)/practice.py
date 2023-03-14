import time
from selenium import webdriver

chrome_driver_path = "C:/Users/charmacist/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url='https://www.amazon.com/')

