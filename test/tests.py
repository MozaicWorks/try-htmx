from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
driver.get("http://127.0.0.1:5000/")

elem = driver.find_element(By.ID,"hello")
assert "No results found." not in driver.page_source

driver.close()
