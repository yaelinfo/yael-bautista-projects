from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://elektra.mx")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div[4]/div/div[2]/div[1]/img'))
)

close_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[4]/div/div[2]/div[1]/img')
close_button.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="downshift-0-input"]'))
)

input_element = driver.find_element(By.XPATH, '//*[@id="downshift-0-input"]')
input_element.clear()
input_element.send_keys("Iphone 17 pro max" + Keys.ENTER)


time.sleep(5)

driver.quit()