from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

text_input = driver.find_element(by=By.NAME, value="my-text")
text_input.send_keys("This is the text input I want selenium to encode")

submit_btn = driver.find_element(by=By.CLASS_NAME, value="btn")
submit_btn.click()



driver.quit()