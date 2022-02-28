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
