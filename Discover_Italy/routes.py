"""
Routes and views for the Discover Italy.
"""

from bottle import route, view, request, redirect
import json
import os
from datetime import datetime
import sys
import io
import re

# кодировка вывода
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# файлы данных
ROUTES_FILE = 'routes_cities.json'
CITIES_FILE = 'cities.json'


# загрузка маршрутов
def load_routes():
    if not os.path.exists(ROUTES_FILE):
        return []
    with open(ROUTES_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return []


# сохранение маршрутов
def save_routes(routes):
    with open(ROUTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(routes, f, ensure_ascii=False, indent=4)


# загрузка городов
def load_cities():
    if not os.path.exists(CITIES_FILE):
        return []
    with open(CITIES_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return []


# генерация id маршрута
def generate_id(routes):
    if not routes:
        return 1
    return max(r.get('id', 0) for r in routes) + 1


@route('/')
@route('/home')
@view('home')
def home():
    return dict(title='Главная')


@route('/contact')
@view('contact')
def contact():
    return dict(title='О разработчиках')


@route('/kitchen')
@view('kitchen')
def kitchen():
    return dict(title='Кухня')


@route('/cities')
@view('cities')
def cities():
    return dict(title='Города')


@route('/active_users')
@view('active_users')
def active_users():
    return dict(title='Активные пользователи')


@route('/articles')
@view('articles')
def articles():
    return dict(title='Статьи')


# страница маршрутов
@route('/new_items')
@view('new_items')
def new_items():
    routes_list = load_routes()
    routes_list.sort(
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M"),
        reverse=True
    )

    cities = load_cities()

    return dict(
        title='Новинки',
        routes=routes_list,
        cities=cities,
        errors={},
        form_data={}
    )

# новинки
@route('/new_items', method='POST')
@view('new_items')
def add_route():
    routes_list = load_routes()
    routes_list.sort(
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M"),
        reverse=True
    )

    cities = load_cities()
    errors = {}

    # получение данных
    name = request.forms.getunicode('route_name', '').strip()
    desc = request.forms.getunicode('description', '').strip()
    c1 = request.forms.getunicode('city1', '')
    c2 = request.forms.getunicode('city2', '')
    c3 = request.forms.getunicode('city3', '')

    form_data = {
        'route_name': name,
        'description': desc,
        'city1': c1,
        'city2': c2,
        'city3': c3
    }

    # валидации
    if not name:
        errors['route_name'] = "Введите название маршрута"
    elif len(name) < 3 or len(name) > 50:
        errors['route_name'] = "От 3 до 50 символов"
    elif not re.match(r'^[A-Za-zА-Яа-я0-9\s\-\,]+$', name):
        errors['route_name'] = "Только буквы и цифры"
    elif not re.search(r'[A-Za-zА-Яа-я]', name):
        errors['route_name'] = "Должна быть хотя бы одна буква"

    if not desc:
        errors['description'] = "Введите описание"
    elif len(desc) < 10 or len(desc) > 300:
        errors['description'] = "От 10 до 300 символов"
    elif not re.search(r'[A-Za-zА-Яа-я]', desc):
        errors['description'] = "Должна быть хотя бы одна буква"

    if c1 == c2 or c1 == c3 or c2 == c3:
        errors['cities'] = "Города не должны повторяться"

    # если ошибки
    if errors:
        return dict(
            title='Новинки',
            routes=routes_list,
            cities=cities,
            errors=errors,
            form_data=form_data
        )

    # создание маршрута
    new_route = {
        'id': generate_id(routes_list),
        'name': name,
        'description': desc,
        'city1': c1,
        'city2': c2,
        'city3': c3,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    routes_list.append(new_route)
    routes_list.sort(
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M"),
        reverse=True
    )

    save_routes(routes_list)

    # очищение формы после успеха
    return dict(
        title='Новинки',
        routes=routes_list,
        cities=cities,
        errors={},
        form_data={}
    )