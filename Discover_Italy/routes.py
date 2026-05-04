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

# загрузка
def load_routes():
    if not os.path.exists(ROUTES_FILE):
        return []
    with open(ROUTES_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return []

# сохранение
def save_routes(routes):
    with open(ROUTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(routes, f, ensure_ascii=False, indent=4)


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


# страница с маршрутами (GET)
@route('/new_items')
@view('new_items')
def new_items():
    routes_list = load_routes()

    # сортировка маршрутов по дате (новые сверху)
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


# обработка добавления нового маршрута (POST)
@route('/new_items', method='POST')
@view('new_items')
def add_route():
    routes_list = load_routes()

    # сортировка перед отображением
    routes_list.sort(
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M"),
        reverse=True
    )

    cities = load_cities()
    errors = {}

    # получение данных из формы
    name = request.forms.getunicode('route_name', '').strip()
    desc = request.forms.getunicode('description', '').strip()
    date = request.forms.getunicode('date', '').strip()

    c1 = request.forms.getunicode('city1', '')
    c2 = request.forms.getunicode('city2', '')
    c3 = request.forms.getunicode('city3', '')

    # сохранение введённых данных
    form_data = {
        'route_name': name,
        'description': desc,
        'date': date,
        'city1': c1,
        'city2': c2,
        'city3': c3
    }

    # проверка названия маршрута
    if not name:
        errors['route_name'] = "Введите название"
    elif len(name) < 3 or len(name) > 50:
        errors['route_name'] = "Название слишком короткое"

    # проверка описания
    if not desc:
        errors['description'] = "Введите описание"
    elif len(desc) < 10:
        errors['description'] = "Описание слишком короткое"

    # проверка формата даты
    if not date:
        errors['date'] = "Введите дату"
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d %H:%M")
        except ValueError:
            errors['date'] = "Формат: ГГГГ-ММ-ДД ЧЧ:ММ"

    # проверка городов (не должны повторяться подряд)
    if c1 == c2 or c2 == c3:
        errors['cities'] = "Города не должны идти подряд"

    # если есть ошибки
    if errors:
        return dict(
            title='Новинки',
            routes=routes_list,
            cities=cities,
            errors=errors,
            form_data=form_data
        )

    # создание нового маршрута
    new_route = {
        'id': generate_id(routes_list),
        'name': name,
        'description': desc,
        'date': date,
        'city1': c1,
        'city2': c2,
        'city3': c3
    }

    # добавление в список
    routes_list.append(new_route)

    # сортировка после добавления
    routes_list.sort(
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M"),
        reverse=True
    )

    # сохранение в файл
    save_routes(routes_list)

    # возврат обновлённой страницы
    return dict(
        title='Новинки',
        routes=routes_list,
        cities=cities,
        errors={},
        form_data={}
    )