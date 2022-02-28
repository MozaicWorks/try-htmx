from test.ToDoListModel import ToDoListModel
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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

    def editFirstItemOfFirstList(self, newText):
        #Experiment with this interaction to test it
        firstItem = self.firstListItems()[0]
        firstItem.click()
        firstItem.text = newText

    def toListModel(self):
        return ToDoListModel(self.firstListHeader().text, self.firstListItemsTexts(), self.firstListAddItemButton().text)
