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
        title='О разработчиках'
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

@route('/active_users')
@view('active_users')
def active_users():
    """Renders the active_users page."""
    return dict(
        title='Активные пользователи'
    )


@route('/new_items')
@view('new_items')
def new_items():
    """Renders the new_items page."""
    return dict(
        title='Новинки'
    )

@route('/articles')
@view('articles')
def articles():
    """Renders the articles page."""
    return dict(
        title='Статьи'
    )