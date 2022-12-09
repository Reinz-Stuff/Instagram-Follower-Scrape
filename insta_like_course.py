from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# ------------ CONSTANTS ------------- #

INS_EMAIL = 'fauzik303@gmail.com'
INS_PASSWORD = 'a4867787'
INS_URL = 'https://www.instagram.com'


class InstaLikers:

    def __init__(self):
        # s = Service('C:/chromedriver.exe')
        # self.driver = webdriver.Chrome(service=s)
        self.driver = webdriver.Chrome('C:/chromedriver.exe')

    def login(self):
        self.driver.get(INS_URL)
        self.driver.maximize_window()

        time.sleep(3)

        username_input_tag = WebDriverWait(self.driver,
                                           10).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//input[@name='username']")))
        username_input_tag.send_keys(INS_EMAIL)

        password_input_tag = WebDriverWait(self.driver,
                                           10).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//input[@name='password']")))
        password_input_tag.send_keys(INS_PASSWORD)
        password_input_tag.send_keys(Keys.ENTER)

    def find_likers(self):
        time.sleep(2)

        self.driver.get('https://www.instagram.com/p/CiTfJPpOW6N/')

        like = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                "//div[@class='_aacl _aaco _aacw _aacx _aada _aade']")))
        like.click()
        time.sleep(5)

        popup = self.driver.find_element(By.CSS_SELECTOR, 'div[style="height: 356px; overflow: hidden auto;"]')

        self.driver.execute_script("window.scrollBy(0,300)", "")
        # self.driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS)

        # Scroll till Followers list is there



if __name__ == '__main__':
    insta_follower_bot = InstaLikers()
    insta_follower_bot.login()
    time.sleep(2)
    insta_follower_bot.find_likers()
