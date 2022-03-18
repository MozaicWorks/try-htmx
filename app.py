from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lists', methods=['GET'])
def lists():
    return render_template("lists.html")

@app.route('/lists/<int:listId>/', methods=['POST'])
def newItem(listId):
    toDoListItems = request.values.to_dict(False)['items[]']
    toDoListItems.append("New Item")
    return render_template('todolist.html', toDoListItems = toDoListItems)

@app.route('/lists/<int:listId>/<int:itemId>/edit', methods=['GET'])
def editFirstItem(listId, itemId):
    toDoListItems = request.values.to_dict(False)['items[]']
    if(itemId != 1):
        beforeItems = toDoListItems[:itemId-1]
        editedItem = toDoListItems[itemId - 1]
        afterItems = toDoListItems[itemId:]
        return render_template('edit-item.html', beforeItems = beforeItems, editedItem = editedItem, afterItems = afterItems)

    editedItem = toDoListItems[itemId - 1]
    displayedItems = toDoListItems[1:]
    return render_template('edit-first-item.html', editedItem = editedItem, displayedItems = displayedItems )

@app.route('/lists/<int:listId>/<int:itemId>/', methods=['POST'])
def saveFirstItem(listId, itemId):
    toDoListItems = request.values.to_dict(False)['items[]']
    return render_template('todolist.html', toDoListItems = toDoListItems)
