"""
Routes and views for the Discover Italyn.
"""

from bottle import route, view

@route('/')
@route('/home')
@view('home')
def home():
    """Renders the home page."""
    return dict(
        title='Главная'
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Контакты'
    )

@route('/kitchen')
@view('kitchen')
def kitchen():
    """Renders the kitchen page."""
    return dict(
        title='Кухня'
    )

@route('/cities')
@view('cities')
def cities():
    """Renders the cities page."""
    return dict(
        title='Города'
    )
