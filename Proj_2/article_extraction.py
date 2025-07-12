from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.gmanetwork.com/news/tracking/politics/")

print(f"page title: {driver.title}")
driver.implicitly_wait(2)
articles = driver.find_elements(by=By.CLASS_NAME, value="story_title")

for article in articles:
    print(article.text, end="\n\n")

driver.quit()