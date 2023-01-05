# import
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 1. LOGIN INSTAGRAM
# arahkan file ke chrome webdriver
driver = webdriver.Chrome('C:/chromedriver.exe')

# buka instagram
driver.get('https://www.instagram.com')
driver.maximize_window()

# target username dan password
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# masukkan username dan password
username.clear()
username.send_keys('fauzik303@gmail.com')
password.clear()
password.send_keys('a4867787')

# arahkan dan klik tombol login
button = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# klik notif popup 1
time.sleep(2)
try:
    alert = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
except:
    pass

# 2. SCRAPE PENCARIAN IG
# cari lokasi input search
try:
    search = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div:nth-child(2) > div > a > div > div > div > div > svg'))).click()
except:
    alert = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    search = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div:nth-child(2) > div > a > div > div > div > div > svg'))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div > input")))
searchbox.clear()

# isi keyword pencarian
keyword = 'remoteworkerid'
searchbox.send_keys(keyword)
time.sleep(2)

# klik hasil pertama di pencarian
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (
        By.CSS_SELECTOR,
        "div > div:nth-child(1) > div > a > div > div._ab8w._ab94._ab99._ab9h._ab9m._ab9o._abcm"))).click()
time.sleep(5)

# SCRAPE LIKE POSTINGAN INTSAGRAM
# scraping link

driver.get('https://www.instagram.com/p/CiTfJPpOW6N/?hl=id')
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='_aacl _aaco _aacw _aacx _aada _aade']"))).click()
time.sleep(5)

# scrolldown pop up
pop_up = driver.find_element(By.CSS_SELECTOR, "div[class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o _ab9s _abcm']")
for run in range(100):
    print(f"scrolling down {run}")
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight'
                          , pop_up)

# output nama ig likers
element_inside_popup = driver.find_elements(By.CSS_SELECTOR, "div[class=' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm']")
ei = []
for i in element_inside_popup:
    print(i.text)
    ei.append(i)
print(len(ei))
