from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lists', methods=['POST'])
def lists():
    return render_template("lists.html")

@app.route('/first-list/add', methods=['POST'])
def newItem():
    toDoListItems = request.values.to_dict(False)['items[]']
    toDoListItems.append("New Item")
    return render_template('todolist.html', toDoListItems = toDoListItems)
