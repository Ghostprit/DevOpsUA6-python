from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.ainonline.com/")
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all("h2", class_="Card_heading___nqQA")
for title in titles:
    print(title.get_text().strip())