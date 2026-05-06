from bottle import route, view, request
from datetime import datetime
import sys
import io

from files_new_items.validation_new_items import validate_route
from files_new_items.storage_new_items import load_routes, save_routes, load_cities, generate_id

# кодировка вывода
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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
    # загрузка маршрутов из файла
    routes_list = load_routes()

    # сортировка маршрутов по дате (новые сверху)
    routes_list.sort(
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M"),
        reverse=True
    )

    # загрузка списка городов
    cities = load_cities()

    # получение данных из формы + очистка пробелов
    name = request.forms.getunicode('route_name', '').strip()
    desc = request.forms.getunicode('description', '').strip()
    date = request.forms.getunicode('date', '').strip()

    # выбранные города
    c1 = request.forms.getunicode('city1', '')
    c2 = request.forms.getunicode('city2', '')
    c3 = request.forms.getunicode('city3', '')

    # сохранение введённыз данных
    form_data = {
        'route_name': name,
        'description': desc,
        'date': date,
        'city1': c1,
        'city2': c2,
        'city3': c3
    }

    # вызов проверки данных
    errors = validate_route(name, desc, date, c1, c2, c3)

    # если есть ошибки — возврат страницы с ошибками
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

    # добавление маршрута в список
    routes_list.append(new_route)

    # повторная сортировка
    routes_list.sort(
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M"),
        reverse=True
    )

    # сохраняем в JSON-файл
    save_routes(routes_list)

    # возвращаем страницу уже с обновлённым списком
    return dict(
        title='Новинки',
        routes=routes_list,
        cities=cities,
        errors={},
        form_data={}
    )