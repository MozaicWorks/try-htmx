import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from parameterized import parameterized 

class EndToEndTests(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        self._driver = webdriver.Firefox(options=options)
        self._driver.get("http://127.0.0.1:5000/")
        self._homePage = HomePage(self._driver)

    @parameterized.expand([
       ("AddNone", 0, ["Item 1"] ), 
       ("AddOnce", 1, ["Item 1", "New Item"] ),
       ("AddTwice", 2, ["Item 1", "New Item", "New Item"] ),
       ("AddThreeTimes", 3, ["Item 1", "New Item", "New Item", "New Item"] ),
   ])
    def test_add_item_to_first_list(self, description, count, items):
        expectedListModel = ToDoListModel("First List", items, "Add Item")
        
        for index in range(count):
            self._homePage.clickAddItemToFirstList()

        self.assertEqual(self._homePage.toListModel(), expectedListModel)

    def tearDown(self):
        self._driver.close()

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

    def toListModel(self):
        return ToDoListModel(self.firstListHeader().text, self.firstListItemsTexts(), self.firstListAddItemButton().text)

class ToDoListModel:
    _name: str
    _items: list
    _addLabel: str
    
    def __init__(self, name, items, addLabel):
        self._name = name
        self._items = items
        self._addLabel = addLabel

    def __eq__(self, other):
        return self._name == other._name and \
                self._items == other._items and \
                self._addLabel == other._addLabel

    def __repr__(self):
        return f"ToDoListModel(name={repr(self._name)}, items={repr(self._items)}, addLabel ={repr(self._addLabel)})"


if __name__ == '__main__':
    unittest.main()
