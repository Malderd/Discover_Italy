"""
Routes and views for the Discover Italyn.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('home')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('Контакты')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/kitchen')
@view('kitchen')
def kitchen():
    """Renders the kitchen page."""
    return dict(
        title='Кухня',
        message='Страница кухни',
        year=datetime.now().year
    )

@route('/cities')
@view('cities')
def cities():
    """Renders the cities page."""
    return dict(
        title='Города',
        message='Города Италии',
        year=datetime.now().year
    )
