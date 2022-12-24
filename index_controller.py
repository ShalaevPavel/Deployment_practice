from flask import Flask
app = Flask(__name__)

@app.route('/secret')
def top_secret():
    return 'You found it!'
