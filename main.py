import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

load_dotenv()

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get('https://google.com/')

# googleアカウントのログイン画面へ遷移
google_account_login_button = driver.find_element(By.CLASS_NAME, "gb_1")
google_account_login_button.click()

# googleアカウントにログイン
mail_box = driver.find_element("name", "identifier")
mail_box.send_keys(os.environ['GOOGLE_UESR_NAME'], Keys.ENTER)
driver.implicitly_wait(10)

password_box = driver.find_element("name", "Passwd")
password_box.send_keys(os.environ["GOOGLE_USER_PASSWORD"], Keys.ENTER)
driver.implicitly_wait(10)

driver.quit()
