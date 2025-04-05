from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Открытие смартис
browser = webdriver.Chrome()
browser.get('https://stage.smartis.bi/')

# Авторизация
username_input = browser.find_element(By.ID , 'email')
password_input = browser.find_element(By.ID , 'password')
username_input.send_keys('yu.shepel@smartis.bi')
password_input.send_keys('12345678')
password_input.send_keys(Keys.RETURN)

time.sleep(3)
# Создание нового дашборда
dashboard_create = browser.find_element(By.CSS_SELECTOR , '[class="el-button el-button--btn btn-success el-button--small"]')
dashboard_create.click()

# Имя для нового дашборда
dashboard_name = browser.find_element(By.CSS_SELECTOR , '[class="el-message-box__input"] input')
dashboard_name.send_keys('Test')
dashboard_ok = browser.find_element(By.CSS_SELECTOR , '[class="el-button el-button--default el-button--small el-button--primary "]')
dashboard_ok.click()

time.sleep(1)
# Удаление нового дашборда
dashboard_delete1 = browser.find_element(By.CSS_SELECTOR , '[class="el-button el-button--primary el-button--small el-dropdown-selfdefine"]  i')
dashboard_delete1.click()
dashboard_delete2 = browser.find_element(By.CSS_SELECTOR , '[class="fa fa-trash-o el-icon--left"]')
dashboard_delete2.click()
dashboard_delete3 = browser.find_element(By.CSS_SELECTOR , '[class="el-button el-button--default el-button--small el-button--primary "]')
dashboard_delete3.click()
time.sleep(3)
