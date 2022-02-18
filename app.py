from flask import Flask, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/lists', methods=['POST'])
def lists():
    return """
        <div id="first-list-container">
            <h1 id="first-list-header">First List</h1>
            <ol id='first-list'>
                <li>Item 1</li>
                <input name="items[]" type="text" value="Item 1"></input>
            </ol>
            <button id="add-item-first-list" hx-post="/first-list/add" hx-trigger="click" hx-target="#first-list-container" hx-include="input">Add Item</button>
        </div>
    """

@app.route('/first-list/add', methods=['POST'])
def newItem():
    items = request.form['items[]']
    return """
            <h1 id="first-list-header">First List</h1>
            <ol id='first-list'>
                <li>Item 1</li>
                <input name="items[]" type="text" value="Item 1"></input>
                <li>Item 2</li>
                <input name="items[]" type="text" value="Item 2"></input>
            </ol>
             <button id="add-item-first-list" hx-post="/first-list/add" hx-trigger="click" hx-target="#first-list-container" hx-include="input">Add Item</button>
    """


