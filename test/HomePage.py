from test.ToDoListModel import ToDoListModel
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self._driver = driver

    def firstListHeader(self):
        return self._driver.find_element(By.ID, "list-header-1")

    def firstListItems(self):
        return self._driver.find_elements(By.CSS_SELECTOR, "#list-1>li")

    def firstListItemsTexts(self):
        return list(map(lambda item: item.text, self.firstListItems()))

    def firstListAddItemButton(self):
        return self._driver.find_element(By.ID, "add-item-list-1")

    def clickAddItemToFirstList(self):
        self.firstListAddItemButton().click()

    def itemEditor(self):
        return self._driver.find_element(By.ID, "list-1-item-edit")

    def itemSave(self):
        return self._driver.find_element(By.ID, "list-1-item-save")

    def editItemOfFirstList(self, index, newText):
        firstItem = self.firstListItems()[index]
        firstItem.click()
        editor = self.itemEditor()
        editor.clear()
        editor.send_keys(newText)
        save = self.itemSave()
        save.click()

    def toListModel(self):
        return ToDoListModel(self.firstListHeader().text, self.firstListItemsTexts(), self.firstListAddItemButton().text)
