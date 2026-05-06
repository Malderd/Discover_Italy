from datetime import datetime

def validate_route(name, desc, date, c1, c2, c3):
    errors = {}

    # проверка названия маршрута
    if not name:
        errors['route_name'] = "Введите название"
    elif len(name) < 3 or len(name) > 50:
        errors['route_name'] = "Название слишком короткое"

    # проверка описания
    if not desc:
        errors['description'] = "Введите описание"
    elif len(desc) < 10:
        errors['description'] = "Описание слишком короткое"

    # проверка формата даты
    if not date:
        errors['date'] = "Введите дату"
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d %H:%M")
        except ValueError:
            errors['date'] = "Формат: ГГГГ-ММ-ДД ЧЧ:ММ"

    # проверка городов
    if c1 == c2 or c2 == c3:
        errors['cities'] = "Города не должны идти подряд"

    return errors
