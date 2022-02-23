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
    toDoListItems = request.values.to_dict(False)['items[]']
    toDoListItems.append("New Item")
    from jinja2 import Template
    j2Template = Template("""
            <h1 id="first-list-header">First List</h1>
            <ol id='first-list'>
            {% for item in toDoListItems %}
                <li>{{item}}</li>
                <input name="items[]" type="hidden" value="{{item}}"></input>
            {% endfor %}
            </ol>
             <button id="add-item-first-list" hx-post="/first-list/add" hx-trigger="click" hx-target="#first-list-container" hx-include="input">Add Item</button>
    """)
    return j2Template.render(toDoListItems = toDoListItems)
