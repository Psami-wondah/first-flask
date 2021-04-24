from flask import Flask
app = Flask(__name__)
@app.route('/')
def greeting():
    return 'Welcome to Your first Flask application'