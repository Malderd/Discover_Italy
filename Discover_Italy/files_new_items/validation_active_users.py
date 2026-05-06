from datetime import datetime
import re

def validate_user(nickname, email, birthdate, gender, tour_number, users):
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
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if email and not re.match(email_pattern, email):
        errors['email'] = "Некорректный email"


    if not birthdate:
        errors['birthdate'] = "Введите дату"
    # дата
    else:
        try:
            datetime.strptime(birthdate, "%d-%m-%Y %H:%M")
        except:
            errors['birthdate'] = "Формат даты: DD-MM-YYYY HH:MM"

    for u in users:
        if u['email'] == email and u['nickname'] != nickname:
            errors['email'] = "Этот email уже используется с другим ником"
            break

    

    return errors