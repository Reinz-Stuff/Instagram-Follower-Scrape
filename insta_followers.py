import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ------------ CONSTANTS ------------- #


# SEARCH_URL = 'https://www.instagram.com/geeks_for_geeks/'

print("login")
INS_EMAIL = input("email: ")
INS_PASSWORD = input("password: ")
INS_URL = 'https://www.instagram.com'
SEARCH_URL = input("instagram url: ")  # 'https://www.instagram.com/geeks_for_geeks/'


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome('C:/chromedriver.exe')

    def login(self):
        self.driver.get(INS_URL)

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

    def find_followers(self):
        time.sleep(2)

        self.driver.get(SEARCH_URL)

        # change the link above to your instagram link

        time.sleep(3)

        followers = WebDriverWait(self.driver,
                                  10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,
                                                                            'followers')))

        # The line above is optional, you can change followers to following

        followers.click()

        time.sleep(3)

        try:
            popup = self.driver.find_element(By.CSS_SELECTOR, '._aano')
        except:
            print('FAILED TO FIND POPUP ELEMENT')
        else:

            print('Popup element is found')

        for run in range(100):
            print(f"scrolling down {run}")
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight'
                                       , popup)
            time.sleep(2)

        follows = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- '
                                                             '_aba8 _abcm"]')
        data = []
        for pop in follows:
            follow = pop.find_element(By.CSS_SELECTOR, 'div[class=" _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm"]').text
            urls = pop.find_element(By.CSS_SELECTOR, 'a[class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619'
                                                     ' x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r'
                                                     ' xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq'
                                                     ' x1a2a7pz notranslate _a6hd"]').get_dom_attribute('href')
            data_dict = {
                "follower": follow,
                "Ig link": INS_URL + urls
            }
            data.append(data_dict)

        # Create CSV and excell
        new_search = SEARCH_URL.replace("https://www.instagram.com/", "").replace("/", "")
        df = pd.DataFrame(data)
        df.to_csv(f'result/{new_search}_followers.csv', index=False)
        df.to_excel(f'result/{new_search}_followers.xlsx', index=False)
        df.to_json(f'result/{new_search}_followers.json')


insta_follower_bot = InstaFollower()
insta_follower_bot.login()
time.sleep(2)
insta_follower_bot.find_followers()
