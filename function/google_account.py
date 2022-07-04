from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()


def login(user_name: str, password: str, driver) -> None:
    driver.get('https://google.com/')
    google_account_login_button = driver.find_element(By.CLASS_NAME, "gb_1")
    google_account_login_button.click()

    # googleアカウントにログイン
    mail_box = driver.find_element("name", "identifier")
    mail_box.send_keys(user_name, Keys.ENTER)
    driver.implicitly_wait(10)

    password_box = driver.find_element("name", "Passwd")
    password_box.send_keys(password, Keys.ENTER)
    driver.implicitly_wait(10)
    return
