from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Edge("msedgedriver.exe")
        self.username = username
        self.password = password
        self.i = 2

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)

        self.browser.get("https://www.instagram.com/explore/people/suggested/")
        time.sleep(4)
        #loginClick = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        #loginClick.click()
        i = 1
        while i <= 5:
            kisi = self.browser.find_element_by_xpath(f'// *[ @ id = "react-root"] / section / main / div / div[2] / div / div / div[{i}] / div[3] / button')
            kisi.click()
            time.sleep(2)
            i = i + 1



    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector('div[role=dialog] ul')
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followerCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)


    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Mesaj Gönder":
            followButton.click()
            time.sleep(2)
        else:
            print("Kullanıcıyı zaten takip ediyorsunuz.")
        print(followButton.text)

instagram = Instagram(username, password)
instagram.signIn()
#instagram.getFollowers()
#instagram.followUser("ahmetnihatekici")




