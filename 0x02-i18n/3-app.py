#!/usr/bin/env python3
"""
rovide the correct value for each message ID for each language
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """configuration of the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """return the preferred user's language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """return homepage of the app"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
