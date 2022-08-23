from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Edge("msedgedriver.exe")
        self.username = username
        self.password = password
        self.i = 0

    def signIn_and_five_follow(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(9)

        self.browser.get("https://www.instagram.com/explore/people/suggested/")
        time.sleep(4)
        i = 1
        while i <= 5:
            person = self.browser.find_element_by_xpath(f'// *[ @ id = "react-root"] / section / main / div / div[2] / div / div / div[{i}] / div[3] / button')
            person.click()
            time.sleep(2)
            i = i + 1


instagram = Instagram(username, password)
instagram.signIn_and_five_follow()