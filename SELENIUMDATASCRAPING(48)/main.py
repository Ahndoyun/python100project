from selenium import webdriver

chrome_driver_path = "C:/Users/charmacist/Program Files/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url='https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463')
# price = driver.find_element_by_id("priceblock_ourprice")

# print(price.text)

