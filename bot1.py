# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Open the Website
driver.get('https://ir-appointment.visametric.com/ir')
print('>>>>>>>>>>>>>>>', driver.title)

checkBox = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-checkmark")
checkBox.click()

schengenBtn = driver.find_element(By.ID, "schengenBtn")
schengenBtn.click()


time.sleep(5)
driver.quit()
