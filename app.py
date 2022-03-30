from flask import Flask, url_for, redirect, request, render_template
from templated import templated
from models import Models

app = Flask(__name__)

@app.route('/')
@templated()
def index():
    return Models().index()

@app.route('/lists', methods=['GET'])
@templated()
def lists():
    return Models().lists()

@app.route('/lists/<int:listId>/', methods=['POST'])
@templated('todolist.html')
def newItem(listId):
    return Models().newItem(getItemsListFromRequest(request))

@app.route('/lists/<int:listId>/<int:itemId>/edit', methods=['GET'])
@templated('edit-item.html')
def editItem(listId, itemId):
    return Models().editItem(getItemsListFromRequest(request), listId, itemId)

@app.route('/lists/<int:listId>/<int:itemId>/', methods=['POST'])
@templated('todolist.html')
def saveItem(listId, itemId):
    return Models().saveItem(getItemsListFromRequest(request), listId, itemId)

def getItemsListFromRequest(request):
    return request.values.to_dict(False)['items[]']
