#Created by WilliamOtieno


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://lbry.tv/')

searchbox = driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div[1]/div/div/input')
searchbox.send_keys('Arch Linux')
searchbox.send_keys(Keys.RETURN)


