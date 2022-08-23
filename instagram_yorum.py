from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#windows_path= "C:\\Users\\user\\OneDrive\\Masaüstü\\chromedriver.exe"
browser=webdriver.Edge("msedgedriver.exe")
time.sleep(5)

browser.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

usernameInput = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
passwordInput = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

usernameInput.send_keys(username)
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)
time.sleep(10)

onay = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
onay.click()
time.sleep(5)

onay2 = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
onay2.click()
time.sleep(2)


mesaj=browser.find_element_by_css_selector("//*[@id='react-root']/section/main/section/div/div[2]/div/article[1]/div[3]/section[3]/div/form/textarea")
#search=browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
mesaj.send_keys(".....")
#mesaj.send_keys(Keys.ENTER)