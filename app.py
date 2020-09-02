import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome !"

@app.route('/about')
def hello():
    return 'A Simple Flask Program'

if __name__ == "__main__":
    app.run()