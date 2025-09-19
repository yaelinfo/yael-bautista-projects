from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

refresh_button_xp = "//button[@id='refresh']"
input_mail_xp = "//input[@id='login']"
wait_time = 5

def getOTP(mail, driver):
    driver.execute_script("window.open('https://yopmail.com/en/', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])

    # 1. Escribir correo
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, input_mail_xp))
    )
    login = driver.find_element(By.XPATH, input_mail_xp)
    login.send_keys(mail + Keys.ENTER)

    # 2. Esperar a que aparezca la bandeja (iframe ifinbox)
    WebDriverWait(driver, wait_time).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "ifinbox"))
    )

    # 3. Dar clic en el primer correo
    first_mail = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='m']//span"))
    )
    first_mail.click()

    # 4. Volver al contenido principal y cambiar al iframe ifmail
    driver.switch_to.default_content()
    WebDriverWait(driver, wait_time).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "ifmail"))
    )

    # 5. Ahora sí buscar el div con el OTP
    otp_elem = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(., 'Su clave de acceso')]"))
    )
    otp_text = otp_elem.text

    # 6. Extraer solo el número
    import re
    match = re.search(r"\d{4,}", otp_text)
    otp = match.group(0) if match else None

    driver.switch_to.default_content()
    driver.switch_to.window(driver.window_handles[0])
    return otp
