from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/hello', methods=['POST'])
def hello_world():
    return 'Hello, World!'
