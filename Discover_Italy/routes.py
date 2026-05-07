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

# импорт функций для страницы "Новинки"
from files_new_items.validation_new_items import validate_route
from files_new_items.storage_new_items import load_routes, save_routes, load_cities, generate_id

# кодировка вывода
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# файлы данных
ROUTES_FILE = 'routes_cities.json'
CITIES_FILE = 'cities.json'
ARTICLES_FILE = 'articles.json'

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

# загрузка статей
def load_articles():
    if not os.path.exists(ARTICLES_FILE):
        return []
    with open(ARTICLES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# сохранение статей
def save_articles(articles):
    with open(ARTICLES_FILE, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

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