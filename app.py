from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/lists', methods=['POST'])
def lists():
    return """
        <h1 id="first-list-header">First List</h1>
        <ol id='first-list'>
            <li>Item 1</li>
        </ol>
        <button id="add-item-first-list" hx-post="/first-list/add" hx-trigger="click" hx-target="#lists">Add Item</button>
    """

@app.route('/first-list/add', methods=['POST'])
def newItem():
    return """
        <h1 id="first-list-header">First List</h1>
        <ol id='first-list'>
            <li>Item 1</li>
            <li>Item 2</li>
        </ol>
        <button id="add-item-first-list" hx-post="/first-list/add" hx-trigger="click" hx-target="#lists">Add Item</button>
    """


