import json
import os

# файлы с информацией
BASE_DIR = os.path.dirname(__file__)

ROUTES_FILE = os.path.join(BASE_DIR, 'routes_cities.json')
CITIES_FILE = os.path.join(BASE_DIR, 'cities.json')


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
