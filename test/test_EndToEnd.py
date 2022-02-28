import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class EndToEndTests(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        self._driver = webdriver.Firefox(options=options)
        self._driver.get("http://127.0.0.1:5000/")
        self._homePage = HomePage(self._driver)

    def test_empty_list_created_correctly_on_first_call(self):
        self.assertEmptyListCreated(self._homePage)

    def test_add_item_to_first_list(self):
        driver = self._driver
        firstListAddItemButton = driver.find_element(By.ID, "add-item-first-list")

        firstListAddItemButton.click()

        firstListItems = driver.find_elements(By.CSS_SELECTOR, "#first-list>li")
        self.assertEqual(2, len(firstListItems))

        firstListAddItemButton = driver.find_element(By.ID, "add-item-first-list")
        firstListAddItemButton.click()

        firstListItems = driver.find_elements(By.CSS_SELECTOR, "#first-list>li")
        self.assertEqual(3, len(firstListItems))


    def tearDown(self):
        self._driver.close()

    def assertEmptyListCreated(self, homePage):
        self.assertEqual("First List", homePage.firstListHeader().text)
        self.assertListEqual(homePage.firstListItemsTexts(), ["Item 1"])
        self.assertEqual("Add Item", homePage.firstListAddItemButton().text)

class HomePage:
    def __init__(self, driver):
        self._driver = driver

    def firstListHeader(self): 
        return self._driver.find_element(By.ID, "first-list-header")

    def firstListItems(self):
        return self._driver.find_elements(By.CSS_SELECTOR, "#first-list>li")

    def firstListItemsTexts(self):
        return list(map(lambda item: item.text, self.firstListItems()))

    def firstListAddItemButton(self):
        return self._driver.find_element(By.ID, "add-item-first-list")

if __name__ == '__main__':
    unittest.main()
