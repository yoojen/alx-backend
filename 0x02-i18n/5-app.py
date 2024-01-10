#!/usr/bin/env python3
"""
force a particular locale by passing the locale=fr parameter
"""
from flask import Flask, request, render_template,g
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


@babel.localeselector
def get_locale():
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


def get_user(user_id):
    """return user based on user id"""
    return users.get(int(user_id), 0)


@app.before_request
def before_request():
    """add user to globa object g"""
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    return homepage of the app
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
