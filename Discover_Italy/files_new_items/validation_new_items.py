from datetime import datetime
import re

# проверка на латиницу
latin_pattern = r'[A-Za-z]'

# только спецсимволы
symbols_pattern = r'^[^А-Яа-яЁё0-9]+$'

def validate_route(name, desc, date, c1, c2, c3):
    errors = {}

    # проверка названия маршрута
    if not name:
        errors['route_name'] = "Введите название маршрута"
    elif re.search(latin_pattern, name):
        errors['route_name'] = "Английские буквы запрещены"
    elif name.isdigit():
        errors['route_name'] = "Название должно содержать буквы"
    elif re.match(symbols_pattern, name):
        errors['route_name'] = "Название не состоит из символов"
    elif len(name) < 3 or len(name) > 50:
        errors['route_name'] = "Название короткое/длинное"

    # проверка описания
    if not desc:
        errors['description'] = "Введите описание маршрута"
    elif re.search(latin_pattern, desc):
        errors['description'] = "Английские буквы запрещены"
    elif desc.isdigit():
        errors['description'] = "Описание должно содержать буквы"
    elif re.match(symbols_pattern, desc):
        errors['description'] = "Описание не состоит из символов"
    elif len(desc) < 10:
        errors['description'] = "Описание слишком короткое"

    # дата
    if not date:
        errors['date'] = "Введите дату"
    else:
        try:
            route_date = datetime.strptime(date, "%Y-%m-%d %H:%M")

            # проверка года
            if route_date.year < 2025:
                errors['date'] = "Дата не может быть меньше 2025 года"
            elif route_date.year > 2030:
                errors['date'] = "Дата не может быть больше 2030 года"

        except ValueError:
            errors['date'] = "Формат даты: ГГГГ-ММ-ДД ЧЧ:ММ"

    # города
    if c1 == c2 or c2 == c3:
        errors['cities'] = "Города не должны идти подряд"

    return errors