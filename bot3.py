from selenium import webdriver

from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get("https://ir-appointment.visametric.com/ir")
print(driver.title)

driver.quit()