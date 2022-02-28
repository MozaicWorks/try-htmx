from test.HomePage import HomePage
from test.ToDoListModel import ToDoListModel
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from parameterized import parameterized 

class EndToEndTests(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        self._driver = webdriver.Firefox(options=options)
        self.addCleanup(self._driver.quit)
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

    # Ignored - todo for next time!!!
    def _test_edit_first_item_of_first_list(self):
        expectedListModel = ToDoListModel("First List", ["Milk"], "Add Item")

        self._homePage.editFirstItemOfFirstList("Milk")

        self.assertEqual(self._homePage.toListModel(), expectedListModel)

    def tearDown(self):
        self._driver.close()

if __name__ == '__main__':
    unittest.main()
