from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Yopmail_Get_OTP import getOTP
import time

driver = webdriver.Chrome()
driver.get("https://elektra.mx")

close_button_xpath = "/html/body/div[2]/div/div[1]/div/div[4]/div/div[2]/div[1]/img"
completa_perfil_nombre_xp = "//input[@id='nombre']"
completa_perfil_apellido_xp = "//input[@id='apellido']"
completa_perfil_telefono_xp = "//input[@id='telefono']"
completa_perfil_curp_xp = "//input[@id='curp']"

ymail = "automation_chrome_ekt_register_001"
password = "Huevos99"
completaP_nombre = "Prueba"
completaP_apellido = "Automation"
completaP_telefono = "5555555555"
completaP_curp = ""

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

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Crear cuenta"))
)

crear_cuenta = driver.find_element(By.PARTIAL_LINK_TEXT, "Crear cuenta")
crear_cuenta.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
)

email = driver.find_element(By.XPATH, "//input[@id='email']")
email.send_keys(ymail+"@yopmail.com" + Keys.ENTER)
continuar = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/div[7]/div/div/div/div/div[2]/div[2]/form/button"))
)

continuar.click()

input_otp = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="input-0"]'))
)

##Yopmail search
otp = getOTP(ymail, driver)

input_otp.send_keys(otp)

input_password1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@id='password'])[1]"))
)
input_password1.send_keys(password)

input_password2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@id='password'])[2]"))
)
input_password2.send_keys(password)

finalizar_ccuenta = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html[@class='vtex-elektra']/body[@class='bg-base']/div[@class='render-container render-route-vtex-store-2-x-store-custom-Login']/div[@class='render-provider']/div[@class='vtex-store__template bg-base']/div[@class='flex flex-column min-vh-100 w-100']/div[7]/div[@class='flex flex-grow-1 w-100 flex-column']/div[@class='vtex-render__container-id-custom-login']/div[@class='elektra-custom-login-3tJCKAE_q1ik_25pmgBrkj']/div[@class='elektra-custom-login-ZJE0jcXAFFfAL6_S6fIHx']/div[@class='elektra-custom-login-aK_sSYfhvH87BB7s10ttV']/div[@class='elektra-custom-login-34xE49HWH_3kFe6sy7EQMX']/div/form/button[@class='elektra-custom-login-2t4aswiDHYVTFsEWwqw4r']"))
)

finalizar_ccuenta.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, completa_perfil_nombre_xp))
)

driver.find_element(By.XPATH, completa_perfil_nombre_xp).send_keys(completaP_nombre)
driver.find_element(By.XPATH, completa_perfil_apellido_xp).send_keys(completaP_apellido)
driver.find_element(By.XPATH, completa_perfil_telefono_xp).send_keys(completaP_telefono)
driver.find_element(By.XPATH, completa_perfil_curp_xp).send_keys(completaP_curp)

finalizar_registro = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html[@class='vtex-elektra']/body[@class='bg-base']/div[@class='render-container render-route-vtex-store-2-x-store-custom-Login']/div[@class='render-provider']/div[@class='vtex-store__template bg-base']/div[@class='flex flex-column min-vh-100 w-100']/div[7]/div[@class='flex flex-grow-1 w-100 flex-column']/div[@class='vtex-render__container-id-custom-login']/div[@class='elektra-custom-login-3tJCKAE_q1ik_25pmgBrkj']/div[@class='elektra-custom-login-ZJE0jcXAFFfAL6_S6fIHx']/div[@class='elektra-custom-login-aK_sSYfhvH87BB7s10ttV']/div[@class='elektra-custom-login-fdsU-XeNTaEIuOcI9UpPH']/form/button[@class='elektra-custom-login-1Pxcq0bJFlWv5zvmYF2YER']"))
)
finalizar_registro.click()

nombre_registro_final = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//b[@id='userNamePlaceHolder']"))
)

driver.quit()