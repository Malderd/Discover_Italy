from datetime import datetime
import re
import unittest

special_symbols_pattern = r'^[а-яА-ЯёЁa-zA-Z0-9\s]+$'  # Исправлено: добавил + и начало/конец строки
puncuation_pattern = r'^[a-zA-Z0-9\s.,!?\'"-]+$'
digits_pattern = r'^\d+$'

def validate_articles(author, title, content, date):
    errors = {}
    
    # проверка имени автора
    if not author:
        errors['author'] = "Введите автора"
    elif not re.match(special_symbols_pattern, author):
        errors['author'] = "Имя может содержать только английские и русские буквы и цифры"
    elif len(author) < 3 or len(author) > 40:
        errors['author'] = "Имя не может быть короче 3 символов и не длиннее 40"
    elif re.match(digits_pattern, author):
        errors['author'] = "Имя автора не может содержать только цифры"

    # проверка названия статьи
    if not title:
        errors['title'] = "Введите название статьи"
    elif not re.match(special_symbols_pattern, title):  # Исправлено: должно быть not re.match
        errors['title'] = "Название статьи может содержать только английские и русские буквы, цифры и пробелы"
    elif len(title) < 3 or len(title) > 100:
        errors['title'] = "Название статьи не может быть короче 3 символов и не длиннее 100"
    elif re.match(digits_pattern, title):
        errors['title'] = "Название статьи не может содержать только цифры"

    # проверка статьи
    if not content:
        errors['content'] = "Введите текст статьи"
    elif not re.match(special_symbols_pattern, content):  # Исправлено
        errors['content'] = "Статья может содержать только английские и русские буквы, цифры и пробелы"
    elif len(content) < 20:
        errors['content'] = "Статья не может быть короче 20 символов"
    elif re.match(digits_pattern, content):
        errors['content'] = "Статья не может содержать только цифры"

    # проверка даты
    if not date:
        errors['date'] = "Введите дату"
    else:
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            if date_obj < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
                errors['date'] = "Дата не может быть в прошлом"
        except ValueError:
            errors['date'] = "Неверный формат даты. Используйте ГГГГ-ММ-ДД"

    return errors