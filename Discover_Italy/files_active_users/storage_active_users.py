import os
import json
from datetime import datetime, timedelta


# Определение пути к файлу users.json
base_dir = os.path.dirname(__file__)
user_file = os.path.join(base_dir, 'users.json')

# Загрузка пользователей
def load_users():
    if not os.path.exists(user_file):
        return []
    with open(user_file, 'r', encoding='utf-8') as f:
        try:
            return json.load(f) # Возвращение json в python-объект
        except:
            return [] # Возвращение пустого списка


# Сохранение пользователей
def save_users(users):
    with open(user_file, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

# Поиск активных пользователей
def get_active_users(users):
    active_users = []
    now = datetime.now()
    month6_ago = now - timedelta(days=182)

    # Перебор пользователей
    for user in users:
        recent_tours = []
        # Проверка туров пользователя
        for tour in user['tours']:
            booking_date = datetime.strptime(
                tour['booking_date'],
                "%Y-%m-%d %H:%M"
            )
            # Проверка активности
            if booking_date >= month6_ago:
                recent_tours.append(tour)

        if recent_tours:
            user['recent_tours'] = recent_tours
            active_users.append(user)

    return active_users