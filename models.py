class Models:
    def index(self):
        return {}

    def lists(self):
        return {}

    def newItem(self, items):
        return {'items': items + ["New Item"]}

    def editItem(self, items, listId, itemId):
        return self.splitListInBeforeCurrentAfter(items, itemId)

    def saveItem(self, items, listId, itemId):
        return {'items': items}

    def splitListInBeforeCurrentAfter(self, itemList, itemIndex):
        return {
            'before': itemList[:itemIndex-1], 
            'current': itemList[itemIndex - 1], 
            'after': itemList[itemIndex:]
           }
