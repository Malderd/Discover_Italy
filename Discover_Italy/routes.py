"""
Routes and views for the Discover Italy.
"""

from bottle import route, view, request, redirect
import json
import os
from bottle import route, view, request
from datetime import datetime
import sys
import io

# импорт для "Статьи"
from files_articles.validation_articles import validate_articles
from files_articles.storage_articles import load_articles,save_articles

# импорт для "Бронирование"
from files_active_users.storage_active_users import load_users, save_users, get_active_users
from files_active_users.validation_active_users import validate_user

# импорт функций для страницы "Новинки"
from files_new_items.validation_new_items import validate_route
from files_new_items.storage_new_items import load_routes, save_routes, load_cities, generate_id

# кодировка вывода
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# файлы данных
ROUTES_FILE = 'routes_cities.json'
CITIES_FILE = 'cities.json'
ARTICLES_FILE = 'articles.json'

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

    users = get_active_users(users)

    users = sorted(users, key=lambda u: len(u['recent_tours']), reverse = True)

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
    routes = load_routes()

    nickname = request.forms.get('nickname', '').strip()
    email = request.forms.get('email', '').strip()
    gender = request.forms.get('gender', '').strip()
    tour_number = request.forms.get('tour_number', '').strip()
    tour_date  = request.forms.get('tour_date', '').strip()

    form_data = {
        'nickname': nickname,
        'email': email,
        'gender': gender,
        'tour_number': tour_number,
        'tour_date': tour_date
    }

    errors = validate_user(nickname, email, gender,
                          tour_number, tour_date, users, routes)

    if errors:

        users = get_active_users(users)

        users = sorted(users, key=lambda u: len(u['recent_tours']),
                  reverse = True)

        return dict(
            title='Активные пользователи',
            users=users,
            errors=errors,
            form_data=form_data
        )

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    user = None
    for u in users:
        if u['email'] == email:
            user = u
            break

    if user:
        user['tours'].append({
            'tour_number': tour_number,
            'booking_date': now,
            'tour_date': tour_date
        })

    else:
         users.append({
             'nickname': nickname,
             'email': email,
             'gender': gender,
             'tours': [
                 {
                    'tour_number': tour_number,
                    'booking_date': now,
                    'tour_date': tour_date
                 }
            ]
        })

    save_users(users)

    users = get_active_users(users)

    users = sorted(users, key=lambda u: len(u['recent_tours']),
                  reverse = True)


    return dict(
        title='Активные пользователи',
        users=users,
        errors={},
        form_data={}
    )

@route('/articles', method=['GET', 'POST'])
@view('articles')
def articles():
    articles_list = load_articles()
    
    # сортировка: новые сверху
    articles_list = sorted(
        articles_list,
        key=lambda x: x.get('date', ''),
        reverse=True
    )
    
    error = None
    old = {}
    
    if request.method == 'POST':
        # получение данных из формы + очистка пробелов
        author = request.forms.getunicode('author', '').strip()
        title = request.forms.getunicode('title', '').strip()
        content = request.forms.getunicode('content', '').strip()
        date = request.forms.getunicode('date', '').strip()
        
        # сохранение введённых данных
        old = {
            'author': author,
            'title': title,
            'content': content,
            'date': date
        }
        
        # валидация
        if not author or not title or not content:
            error = "Заполните все поля (автор, заголовок, содержание)"
        
        # если ошибок нет — создаём статью
        if not error:
            # если дата не указана, используем текущую
            if not date:
                date = datetime.now().strftime("%Y-%m-%d %H:%M")
            
            new_article = {
                "author": author,
                "title": title,
                "content": content,
                "date": date
            }
            
            # добавляем в начало списка (новые сверху)
            articles_list.insert(0, new_article)
            
            # сохраняем в JSON-файл
            save_articles(articles_list)
            
            # очищаем форму после успешного добавления
            old = {}
            error = None
            
            # повторная сортировка
            articles_list = sorted(
                articles_list,
                key=lambda x: x.get('date', ''),
                reverse=True
            )
    
    return dict(
        title='Статьи',
        articles=articles_list,
        error=error,
        old=old
    )


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

    cities = load_cities() # загрузка городов

    # отображение страницы
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

    
    # сортировка по дате
    if routes_list:
        try:
            routes_list = sorted(
                routes_list,
                key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M"),
                reverse=True
            )
        except:
            pass
    
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