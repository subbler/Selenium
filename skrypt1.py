from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.wsb.pl")
driver.maxymize_window()

sleep(5)
driver.close()
