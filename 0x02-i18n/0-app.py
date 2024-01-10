#!/usr/bin/env python3
"""
 setup a basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """return string on the home of web using template"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
