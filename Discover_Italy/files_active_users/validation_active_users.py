from datetime import datetime
import re

def validate_user(nickname, email, birthdate, gender, tour_number, users, routes):
    errors = {}

    # Пустые поля
    if not nickname:
        errors['nickname'] = "Введите ник"

    if not email:
        errors['email'] = "Введите email"

    if not birthdate:
        errors['birthdate'] = "Введите дату"

    if not tour_number:
        errors['tour_number'] = "Введите номер тура"

    # Почта
    email_pattern = r'^[a-zA-Z]{1}[a-zA-Z0-9._%+-]{1,50}@[a-zA-Z0-9-]{2,35}\.[a-zA-Z]{2,20}$'
    if email and not re.match(email_pattern, email):
        errors['email'] = "Некорректный email"


    if not birthdate:
        errors['birthdate'] = "Введите дату"
    # дата
    else:
        try:
            datetime.strptime(birthdate, "%Y-%m-%d %H:%M")
        except:
            errors['birthdate'] = "Формат даты: ГГГГ-ММ-ДД ЧЧ:ММ"

    for u in users:
        if u['email'] == email and u['nickname'] != nickname:
            errors['email'] = "Этот email уже используется с другим ником"
            break

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