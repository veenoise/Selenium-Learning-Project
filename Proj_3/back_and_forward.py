from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.gmanetwork.com/news/tracking/politics/")


# Explicit wait
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda d : len(d.find_elements(by=By.CLASS_NAME, value="story_title")) > 0)
articles = driver.find_elements(by=By.CLASS_NAME, value="story_title")

# Print the article titles
for article in articles:
    print(article.text, end="\n\n")
print(f"\n\n\n\n\n\n")


# Open a link (this link opens new tab)
print(F"Current Tab Title: {driver.title}")
previous_title = driver.title
previous_tab = driver.current_window_handle
articles[0].click()
wait.until(EC.number_of_windows_to_be(2))
for window_handle in driver.window_handles:
    if window_handle != previous_tab:
        new_tab = window_handle
        print(f"Prev tab: {previous_tab}")
        print(f"New_tab: {new_tab}")
        driver.switch_to.window(window_handle)
        break

# Print the title of the new tab
wait.until(lambda d : d.title != previous_title)
print(f"New Tab Title: {driver.title}")

# Go back to the previous tab
driver.switch_to.window(previous_tab)
wait.until(lambda d: d.title == previous_title)
print(f"Previous Tab Title: {driver.title}")

driver.quit()