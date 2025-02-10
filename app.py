from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Gaga...wish you a good day"
