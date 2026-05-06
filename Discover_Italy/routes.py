from bottle import route, view, request
from datetime import datetime
import sys
import io

from files_new_items.storage_active_users import load_users, save_users
from files_new_items.validation_active_users import validate_user

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


# Страница с маршрутами (GET)
@route('/active_users')
@view('active_users')
def active_users():
    users = load_users()
    return dict(
        title='Активные пользователи',
        users=users,
        errors={},
        form_data={}
    )

# Страница с маршрутами (POST)
@route('/active_users', method='POST')
@view('active_users')
def add_users():
    users = load_users()

    nickname = request.forms.get('nickname', '').strip()
    email = request.forms.get('email', '').strip()
    birthdate = request.forms.get('birthdate', '').strip()
    gender = request.forms.get('gender', '').strip()
    tour_number = request.forms.get('tour_number', '').strip()

    form_data = {
        'nickname': nickname,
        'email': email,
        'birthdate': birthdate,
        'gender': gender,
        'tour_number': tour_number
    }

    errors = validate_user(nickname, email, birthdate, gender, tour_number, users)

    if errors:
        return dict(
            title='Активные пользователи',
            users=users,
            errors=errors,
            form_data=form_data
        )

    now = datetime.now().strftime("%d-%m-%Y %H:%M")

    user = None
    for u in users:
        if u['email'] == email:
            user = u
            break

    if user:
        user['tour_numbers'].append(tour_number)
        user['last_tour_datetime'] = now
    else:
        users.append({
            'nickname': nickname,
            'email': email,
            'birthdate': birthdate,
            'gender': gender,
            'tour_numbers': [tour_number],
            'last_tour_datetime': now
        })

    save_users(users)

    return dict(
        title='Активные пользователи',
        users=users,
        errors={},
        form_data={}
    )


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