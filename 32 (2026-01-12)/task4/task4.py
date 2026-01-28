from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--kiosk')
driver = webdriver.Chrome(options=options)

driver.get("https://www.ainonline.com/")
try:
    searchButton = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "DesktopSiteHeader_search-toggle__ZhLAw")))
    searchButton.click()
    searchField = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "header-search")))
    searchField.send_keys("Eurofighter")
    searchField.send_keys(u"\ue007")
finally:
    driver.quit()

