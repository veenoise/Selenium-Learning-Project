from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")
action = ActionChains(driver) 

def click_link():
    link = driver.find_element(by=By.ID, value="click")
    action.click(link)
    action.perform()
    time.sleep(3)

def clickable_field():
    field = driver.find_element(by=By.ID, value="clickable")
    action.move_to_element(field).click().send_keys("hello world")
    action.perform()
    time.sleep(3)

def move_draggable():
    box = driver.find_element(by=By.ID, value="draggable")
    action.click_and_hold(box)
    action.move_by_offset(10, 100)
    action.release()
    action.perform()
    time.sleep(3)

def hover():
    button = driver.find_element(by=By.ID, value="hover")
    action.move_to_element(button)
    action.perform()
    time.sleep(3)
    
def move_relative():
    box = driver.find_element(by=By.ID, value="mouse-tracker")
    action.scroll_by_amount(0, 1000)
    action.pause(1)
    action.move_to_element(box)
    action.pause(2)
    action.move_to_element_with_offset(box, 10, 10)
    action.perform()
    time.sleep(3)

move_relative()