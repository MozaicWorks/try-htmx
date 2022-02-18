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

    def test_empty_list_on_first_call(self):
        driver = self._driver
        driver.get("http://127.0.0.1:5000/")

        listHeader = driver.find_element(By.ID, "first-list-header")
        self.assertEqual("First List", listHeader.text)

        listElement = driver.find_element(By.ID, "first-list")
        assert "No results found." not in driver.page_source

        firstListItems = driver.find_elements(By.CSS_SELECTOR, "#first-list>li")
        self.assertEqual(1, len(firstListItems))

        firstItemOfFirstList = firstListItems[0]
        self.assertEqual("Item 1", firstItemOfFirstList.text)

        firstListAddItemButton = driver.find_element(By.ID, "add-item-first-list")
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self._driver.close()

if __name__ == '__main__':
    unittest.main()
