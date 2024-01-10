#!/usr/bin/env python3
"""
force a particular locale by passing the locale=fr parameter
"""
from flask import Flask, request, render_template, globals
from flask_babel import Babel


class Config(object):
    """
    configuration class of whole application
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user(user_id):
    """return user based on user id"""
    if users.get(user_id) is not None:
        return users.get(user_id)
    return None


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale/lang from request params
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """add user to globa object g"""
    user_id = request.args.get('login_as')
    user = get_user(user_id)
    setattr(globals.g, 'user', user)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    return homepage of the app
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
