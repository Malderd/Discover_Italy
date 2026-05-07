from datetime import datetime
import re

email_pattern = r'^[a-zA-Z]{1}[a-zA-Z0-9._%+-]{1,50}@[a-zA-Z0-9-]{2,35}\.[a-zA-Z]{2,20}$'
nickname_pattern = r'^[a-zA-Z]{1}[a-zA-Z0-9]{4,30}'

def validate_user(nickname, email, gender, tour_number, tour_date, users, routes):
    errors = {}

    # Пустые поля
    if not nickname:
        errors['nickname'] = "Введите ник"

    if not email:
        errors['email'] = "Введите email"

    if not tour_number:
        errors['tour_number'] = "Введите номер тура"

    if not tour_date:
        errors['tour_date'] = "Введите дату тура"

    # Проверка ника
    if validate_nickname(nickname) == False:
        errors['nickname'] = "Некорректный ник"

    # Проверка почты
    if validate_email(email) == False:
        errors['email'] = "Некорректный email"

    # Проверка формата даты тура
    if validate_tour_date(tour_date) == False:
            errors['tour_date'] = "Формат даты: ГГГГ-ММ-ДД ЧЧ:ММ"

    # Проверка, что дата тура больше текущего дня
    if validate_tour_date_after_now(tour_date) == False:
        errors['tour_date'] = "Дата тура должна быть раньше текущего дня"

    for u in users:
        if u['email'] == email and u['nickname'] != nickname:
            errors['email'] = "Этот email уже используется с другим ником"
            break

    for u in users:
        if u['email'] == email and u['nickname'] == nickname:
            if u['gender'] != gender:
                errors['gender'] = "Нельзя изменить пол для существующего пользователя"
                break

    found = False

    for r in routes:
        if str(r['id']) == str(tour_number):
            found = True
            break

    if not found:
        errors['tour_number'] = "Такого тура не существует"

    return errors

def validate_email(email):
    if (re.match(email_pattern, email)):
        return True
    else:
        return False

def validate_nickname(nickname):
    if (re.match(nickname_pattern, nickname)):
        return True
    else:
        return False

def validate_tour_date_after_now(tour_date):
    if str(tour_date) > datetime.now().strftime("%Y-%m-%d %H:%M"):
        return True
    else:
        return False


def validate_tour_date(tour_date):
    try:
        datetime.strptime(tour_date, "%Y-%m-%d %H:%M")
        return True
    except:
        return False