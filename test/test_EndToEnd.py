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
        self.assertListIs(self._homePage, "First List", ["Item 1"], "Add Item")

    def test_add_item_to_first_list(self):
        self._homePage.clickAddItemToFirstList()
        self.assertListIs(self._homePage, "First List", ["Item 1", "New Item"], "Add Item")

        self._homePage.clickAddItemToFirstList()
        self.assertListIs(self._homePage, "First List", ["Item 1", "New Item", "New Item"], "Add Item")

    def tearDown(self):
        self._driver.close()

    def assertListIs(self, homePage, listName, listItemsTexts, addItemLabel):
        self.assertEqual(listName, homePage.firstListHeader().text)
        self.assertListEqual(homePage.firstListItemsTexts(), listItemsTexts)
        self.assertEqual(addItemLabel, homePage.firstListAddItemButton().text)

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

    def clickAddItemToFirstList(self):
        self.firstListAddItemButton().click()

if __name__ == '__main__':
    unittest.main()
