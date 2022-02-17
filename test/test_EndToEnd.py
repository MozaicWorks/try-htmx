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

        listElement = driver.find_element(By.ID, "1")
        assert "No results found." not in driver.page_source

        listHeader = driver.find_element(By.ID, "First")
        assert "No results found." not in driver.page_source

        self.assertEqual("First List", listHeader.text)

        #elem.click()
        #replacedText = driver.find_element(By.XPATH, "//body")
        #self.assertEqual(replacedText.text, "Hello, World!")

    def tearDown(self):
        self._driver.close()

if __name__ == '__main__':
    unittest.main()
