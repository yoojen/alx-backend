#!/usr/bin/env python3
"""
flas application for basic auth
"""
import pytz
from flask import Flask
from flask import g, request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
   configuration of the application
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id):
    """
    return the user if id is found
    """
    return users.get(int(id), {})


@babel.localeselector
def get_locale() -> str:
    """
    try to get locale from the request param
    """
    from_url = request.args.get('locale', '').strip()
    locale_url = g.user.get('locale', None) if g.user else None
    set_preference = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    default_locale = Config.BABEL_DEFAULT_LOCALE
    locale_options = [from_url, locale_url, set_preference, default_locale]

    for locale in locale_options:
        if locale and locale in Config.LANGUAGES:
            return locale


@babel.timezoneselector
def get_timezone() -> str:
    """
    Gets timezone from request object
    """
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        return pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request() -> None:
    """
    insert verified user to the global object `g`
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    return a html template on screen
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
