"""
Routes and views for the Discover Italy.
"""

from bottle import route, view, request
import json
import os
from datetime import datetime
import sys
import io

# Установка кодировки для добавленяи в json на входе
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Файлы для новинок
ROUTES_FILE = 'routes_cities.json'
CITIES_FILE = 'cities.json'

# Метод загрузки файла маршрутов
def load_routes(): 
    if not os.path.exists(ROUTES_FILE):
        return []
    with open(ROUTES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Метод сохранения маршрутов
def save_routes(routes):
    with open(ROUTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(routes, f, ensure_ascii=False, indent=4)

# Чтение городов из файла для маршрутов
def load_cities():
    if not os.path.exists(CITIES_FILE):
        return []
    with open(CITIES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Генерация id для маршрута
def generate_id(routes):
    if not routes:
        return 1
    return max(r['id'] for r in routes) + 1

# Основные страницы
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


# Страница новинок
@route('/new_items', method=['GET', 'POST'])
@view('new_items')
def new_items():
    routes_list = load_routes()
    cities = load_cities()

    if request.method == 'POST':
        name = request.forms.getunicode('route_name')
        desc = request.forms.getunicode('description')
        c1 = request.forms.getunicode('city1')
        c2 = request.forms.getunicode('city2')
        c3 = request.forms.getunicode('city3')

        # Обработка ошибок
        if not name or not desc:
            return dict(
                title='Новинки',
                routes=routes_list,
                cities=cities,
                error="Заполните все поля"
            )

        if c1 == c2 or c1 == c3 or c2 == c3:
            return dict(
                title='Новинки',
                routes=routes_list,
                cities=cities,
                error="Города не должны повторяться"
            )

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

        routes_list = sorted(routes_list, key=lambda x: x['date'], reverse=True)

        save_routes(routes_list)

        return dict(
            title='Новинки',
            routes=routes_list,
            cities=cities
        )

    return dict(
        title='Новинки',
        routes=routes_list,
        cities=cities
    )