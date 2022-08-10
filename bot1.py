# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the Website
# browser.get('https://ir-appointment.visametric.com/ir')
# browser.get('https://www.python.org/')
# print(browser.title)
browser.quit()
