from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://elektra.mx")

close_button_xpath = "/html/body/div[2]/div/div[1]/div/div[4]/div/div[2]/div[1]/img"

email = "qatesterekt@gmail.com"
password = "Huevos99"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, close_button_xpath))
)

close_button = driver.find_element(By.XPATH, close_button_xpath)
close_button.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Inicia sesión"))
)

inicia_sesion = driver.find_element(By.PARTIAL_LINK_TEXT, "Inicia sesión")
inicia_sesion.click()

##Input mail and password
email_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
)
email_input.send_keys(email)

password_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
)
password_input.send_keys(password)

login_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html[@class='vtex-elektra']/body[@class='bg-base']/div[@class='render-container render-route-vtex-store-2-x-store-custom-Login']/div[@class='render-provider']/div[@class='vtex-store__template bg-base']/div[@class='flex flex-column min-vh-100 w-100']/div[7]/div[@class='flex flex-grow-1 w-100 flex-column']/div[@class='vtex-render__container-id-custom-login']/div[@class='elektra-custom-login-3tJCKAE_q1ik_25pmgBrkj']/div[@class='elektra-custom-login-ZJE0jcXAFFfAL6_S6fIHx']/div[@class='elektra-custom-login-aK_sSYfhvH87BB7s10ttV']/div[@class='elektra-custom-login-DYxB4Or3yYU7LvFXbEbCn']/div[@class='elektra-custom-login-3x3vNd8ddp099olhhQQn_y']/form/button[@class='elektra-custom-login--SZFFHOzoCSNuMzee3YiC']"))
)
login_button.click()

confirm_login = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//b[@id='userNamePlaceHolder']"))
)

driver.quit()