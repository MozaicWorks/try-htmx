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

    def firstListFirstItemEditor(self):
        return self._driver.find_element(By.ID, "first-list-first-item-edit")

    def firstListSecondItemEditor(self):
        return self._driver.find_element(By.ID, "first-list-second-item-edit")

    def firstListFirstItemSave(self):
        return self._driver.find_element(By.ID, "first-list-first-item-save")

    def firstListSecondItemSave(self):
        return self._driver.find_element(By.ID, "first-list-second-item-save")

    def editFirstItemOfFirstList(self, newText):
        firstItem = self.firstListItems()[0]
        firstItem.click()
        firstItemEditor = self.firstListFirstItemEditor()
        firstItemEditor.clear()
        firstItemEditor.send_keys(newText)
        firstItemSave = self.firstListFirstItemSave()
        firstItemSave.click()

    def editSecondItemOfFirstList(self, newText):
        secondItem = self.firstListItems()[1]
        secondItem.click()
        secondItemEditor = self.firstListSecondItemEditor()
        secondItemEditor.clear()
        secondItemEditor.send_keys(newText)
        secondItemSave = self.firstListSecondItemSave()
        secondItemSave.click()

    def toListModel(self):
        return ToDoListModel(self.firstListHeader().text, self.firstListItemsTexts(), self.firstListAddItemButton().text)
