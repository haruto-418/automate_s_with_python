import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

from function.google_account import login

load_dotenv()

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

login(os.environ['GOOGLE_USER_NAME'],
      os.environ["GOOGLE_USER_PASSWORD"], driver)

# google広告にログイン
driver.get("https://ads.google.com/intl/ja_JP/home/")
driver.implicitly_wait(10)

hamburger_btn = driver.find_element(
    By.CLASS_NAME, "glue-header__drawer-toggle-btn")
hamburger_btn.click()

google_ads_login_btn = driver.find_element(By.LINK_TEXT, "ログイン")
google_ads_login_btn.click()

# 終了
driver.quit()
