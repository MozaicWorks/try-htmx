from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5000/")

elem = driver.find_element(By.ID,"hello")
assert "No results found." not in driver.page_source

driver.close()
