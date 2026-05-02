"""
Routes and views for the Discover Italy.
"""

from bottle import route, view, request
import json
import os
from datetime import datetime
import sys
import io

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
        return json.load(f)

# сохранение маршрутов
def save_routes(routes):
    with open(ROUTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(routes, f, ensure_ascii=False, indent=4)


# загрузка городов
def load_cities():
    if not os.path.exists(CITIES_FILE):
        return []
    with open(CITIES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


# генерация id маршрута
def generate_id(routes):
    if not routes:
        return 1
    return max(r['id'] for r in routes) + 1


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
@route('/new_items', method=['GET', 'POST'])
@view('new_items')
def new_items():

    # загрузка маршрутов из файла
    routes_list = load_routes()

    # сортировка по дате
    routes_list = sorted(
        routes_list,
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M"),
        reverse=True
    )

    # загрузка списка городов
    cities = load_cities()

    # обработка формы (добавление маршрута)
    if request.method == 'POST':

        # получение данных формы
        name = request.forms.getunicode('route_name')
        desc = request.forms.getunicode('description')
        c1 = request.forms.getunicode('city1')
        c2 = request.forms.getunicode('city2')
        c3 = request.forms.getunicode('city3')


        # проверка заполнения полей
        if not name or not desc:
            return dict(
                title='Новинки',
                routes=routes_list,
                cities=cities,
                error="Заполните все поля"
            )

        # проверка одинаковых городов
        if c1 == c2 or c1 == c3 or c2 == c3:
            return dict(
                title='Новинки',
                routes=routes_list,
                cities=cities,
                error="Города не должны повторяться"
            )

        # создание нового маршрута
        new_route = {
            'id': generate_id(routes_list),
            'name': name,
            'description': desc,
            'city1': c1,
            'city2': c2,
            'city3': c3,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        # добавление в список
        routes_list.append(new_route)

        # сохранение в файл
        save_routes(routes_list)

        # возврат страницы с отсортированным списком
        return dict(
            title='Новинки',
            routes=routes_list,
            cities=cities
        )

    # открытие страницы
    return dict(
        title='Новинки',
        routes=routes_list,
        cities=cities
    )