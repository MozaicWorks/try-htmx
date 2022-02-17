from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/lists', methods=['POST'])
def lists():
    return """
        <ol id='1'></ol>
    """
