import webbrowser
import time
import pyautogui as gui
from selenium import webdriver
url="https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(15)
position =driver.find_element_by_class_name('whsOnd.zHQkBf')
position.click()
time.sleep(1)
position.send_keys("app@gmail.com")
time.sleep(1)
position =driver.find_element_by_class_name('whsOnd.zHQkBf')
position.send_keys("*******")
time.sleep(1)



