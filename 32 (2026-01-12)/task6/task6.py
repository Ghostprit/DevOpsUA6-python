import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

conn = sqlite3.connect('example.db')
cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS ainonlineNews (id INTEGER PRIMARY KEY, title TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS simpleFlyingNews (id INTEGER PRIMARY KEY, title TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS generalAviationNews (id INTEGER PRIMARY KEY, title TEXT)")

driver = webdriver.Chrome()

driver.get("https://www.ainonline.com/")
try:
    titles = driver.find_elements(By.CLASS_NAME, "Card_heading___nqQA")

    for i in titles[:5]:
        titleText = i.text
        cursor.execute("INSERT INTO ainonlineNews (title) VALUES (?)", (titleText,))
finally:
    driver.quit()

driver = webdriver.Chrome()
driver.get("https://simpleflying.com/category/aviation-news/")
try:
    sfTitles = driver.find_elements(By.CLASS_NAME, "display-card-title ")

    for i in sfTitles[:5]:
        sfTitleText = i.text
        cursor.execute("INSERT INTO simpleFlyingNews (title) VALUES (?)", (sfTitleText,))
finally:
    driver.quit()

driver = webdriver.Chrome()
driver.get("https://generalaviationnews.com/")
try:
    gaNewsTitles = driver.find_elements(By.CLASS_NAME, "entry-title")

    for i in gaNewsTitles[:5]:
        gaTitleText = i.text
        cursor.execute("INSERT INTO generalAviationNews (title) VALUES (?)", (gaTitleText,))
finally:
    driver.quit()

results = cursor.execute("SELECT * FROM ainonlineNews")
for row in results.fetchall():
    print("Ainonline News:", row)

results = cursor.execute("SELECT * FROM simpleFlyingNews")
for row in results.fetchall():
    print("Simple Flying News:", row)

results = cursor.execute("SELECT * FROM generalAviationNews")
for row in results.fetchall():
    print("General Aviation News:", row)

conn.commit()
conn.close()