from datetime import datetime
import re

# Паттерн для email
email_pattern = r'^(?!.*[._%+-]{2})(?!.*[._%+-]@)[a-zA-Z]{1}[a-zA-Z0-9._%+-]{3,50}@[a-zA-Z0-9-]{2,35}\.[a-zA-Z]{2,20}$'

# Паттерн для ника
nickname_pattern = r'^(?!.*[_-]{2})[a-zA-Z]{1}[a-zA-Z0-9_-]{4,30}$'

def validate_user(nickname, email, gender, tour_number, tour_date, users, routes):
    errors = {}

    # Проверка пустых полей
    if not nickname:
        errors['nickname'] = "Введите ник"
    # Проверка ника на соответствие паттерну
    elif validate_nickname(nickname) == False:
        errors['nickname'] = "Некорректный ник"

    if not email:
        errors['email'] = "Введите email"
    # Проверка почты на соответствие паттерну
    elif validate_email(email) == False:
        errors['email'] = "Некорректный email"


    # Проверка формата даты тура
    if validate_tour_date(tour_date) == False:
            errors['tour_date'] = "Формат даты: ГГГГ-ММ-ДД"
    # Проверка, что дата тура больше текущего дня
    elif validate_tour_date_after_now(tour_date) == False:
            errors['tour_date'] = "Дата тура должна быть раньше текущего дня"
    elif validate_year(tour_date) == False:
            errors['tour_date'] = "Дата тура должны быть меньше 2029 года"


    # Провера, что 1 email не может принадлежать разным никак
    for u in users:
        if u['email'] == email and u['nickname'] != nickname:
            errors['email'] = "Этот email уже используется с другим ником"
            break

    # Проверка, если email и ник уже есть в базе, то пол менять нельзя
    for u in users:
        if u['email'] == email and u['nickname'] == nickname:
            if u['gender'] != gender:
                errors['gender'] = "Нельзя изменить пол для существующего пользователя"
                break

    # Проверка существования тура в routes
    found = False

    for r in routes:
        if str(r['id']) == str(tour_number):
            found = True
            break

    if not found:
        errors['tour_number'] = "Такого тура не существует"

    return errors

# Функция проверки email соответствия шаблону
def validate_email(email):
    if (re.match(email_pattern, email)):
        return True
    else:
        return False

# Функция проверки ника соответствия шаблону
def validate_nickname(nickname):
    if (re.match(nickname_pattern, nickname)):
        return True
    else:
        return False

# Функция проверки, что дата тура не меньше текущей даты
def validate_tour_date_after_now(tour_date):
    tour_dt = datetime.strptime(tour_date, "%Y-%m-%d").date()
    if tour_dt >= datetime.now().date():
        return True
    else:
        return False


# Функция проверка даты соответствия формату
def validate_tour_date(tour_date):
    try:
        tour_date = datetime.strptime(tour_date, "%Y-%m-%d")
        return True
    except:
        return False

def validate_year(tour_date):
    try:
        date = tour_date.split("-")
        if int(date[0]) < 2029:
            return True
        else:
            return False
    except:
        return False