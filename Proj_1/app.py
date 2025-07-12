from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://techwithtim.net")

# Print the title of the document
print(driver.title)
driver.quit()