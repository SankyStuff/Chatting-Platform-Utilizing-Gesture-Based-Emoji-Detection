from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import emoji

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window() 
url='http://localhost/chat_project/login.php'
driver.get(url)
loginidpath='//*[@id="email"]'
passwordpath='//*[@id="pwd"]'
loginbutton='/html/body/div/form/div[3]/div/button'
openchatbutton='/html/body/div/center/a'
formwindow='/html/body/div/form/div/div[1]/textarea'
sendbutton='/html/body/div/form/div/div[2]/button'
driver.implicitly_wait(2)
# lid=driver.find_elements("xpath", loginidpath)
driver.find_elements("xpath", loginidpath)[0].click()
# lid.click()
driver.find_elements("xpath", loginidpath)[0].send_keys('sanskar@gmail.com')
driver.find_elements("xpath", passwordpath)[0].click()
driver.find_elements("xpath", passwordpath)[0].send_keys('sanskar')

driver.find_elements("xpath", loginbutton)[0].click()

driver.find_elements("xpath", openchatbutton)[0].click()

driver.find_elements("xpath", formwindow)[0].click()
driver.find_elements("xpath", formwindow)[0].send_keys(emoji.emojize(':victory_hand:'))

sd=driver.find_elements("xpath", sendbutton)[0].click()

driver.close()