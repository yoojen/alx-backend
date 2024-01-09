#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIME_ZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def home():
    """return homepage for the app"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
