# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'D:\\Jorge\\Documents\\UPP\\Pruebas del software\\Kevin\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('http://www.imss.gob.mx/')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'a.u1st_accBtn.u1st_accBtnText')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'a.navbar-brand')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      '.btn.btn-default')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'a.navbar-brand')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'a.nav-link')))\
    .click()

driver.quit()