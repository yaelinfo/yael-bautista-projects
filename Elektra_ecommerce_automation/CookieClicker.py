from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'langSelect-EN'))
)

language_prompt = driver.find_element(By.ID, 'langSelect-EN')
language_prompt.click()

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//button[@id='bigCookie']"))
)

cookie = driver.find_element(By.XPATH, "//button[@id='bigCookie']")
for n in range(10):
    cookie.click()

time.sleep(10)

driver.quit()