import unittest

# импорт валидации для пользователей
from files_active_users import validation_active_users
from files_active_users.validation_active_users import validate_nickname, validate_user
from files_active_users.storage_active_users import load_users
from files_new_items.storage_new_items import load_routes

# импорт валидации для новинок
from files_new_items.validation_new_items import validate_route

# импорт валидации для статей 
from files_articles.validation_articles import validate_articles

# =========================================
# НОВИНКИ
# =========================================
class TestItems(unittest.TestCase):

    def test_items_valid_data(self):
        errors = validate_route(
            "Маршрут 1",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertEqual(errors, {})

    def test_items_empty_name(self):
        errors = validate_route(
            "",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('route_name', errors)

    def test_items_short_description(self):
        errors = validate_route(
            "Маршрут",
            "Коротко",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('description', errors)

    def test_items_invalid_date(self):
        errors = validate_route(
            "Маршрут",
            "Хорошее описание маршрута",
            "06-05-2026",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('date', errors)

    def test_items_invalid_time(self):
        errors = validate_route(
            "Маршрут",
            "Хорошее описание маршрута",
            "2026-06-05 20",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('date', errors)

    def test_items_same_cities(self):
        errors = validate_route(
            "Маршрут",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Рим", "Милан"
        )
        self.assertIn('cities', errors)

    def test_items_name_only_digits(self):
        errors = validate_route(
            "12345",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('route_name', errors)

    def test_items_description_only_digits(self):
        errors = validate_route(
            "Маршрут 1",
            "1234567890",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('description', errors)

    def test_items_name_with_latin(self):
        errors = validate_route(
            "Route 1",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('route_name', errors)

    def test_items_description_with_latin(self):
        errors = validate_route(
            "Маршрут 1",
            "Nice trip in Italy",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('description', errors)
# =========================================
# СТАТЬИ
# =========================================
class TestArticles(unittest.TestCase):
    #проверка, на все правильные введенные данные
    def test_articles_valid_data(self):
        errors = validate_articles(
            "Дорогов",
            "Путешествие по солевой Италии",
            "Отличное путешествие с замечательными людьми",
            "2026-05-16"
        )
        self.assertEqual(errors, {})
        #неверно введенный автор
    def test_articles_author_incorrect(self):
        errors = validate_articles(
            "!!!!@#ljdkkf",
            "Путешествие по красивой Италии",
            "Отличное путешествие с замечательными людьми",
            "2026-05-09"
        )
        self.assertIn('author', errors)
     # в заголовке только цифры
    def test_articles_title_incorrect(self):
        errors = validate_articles(
            "Ладушка67",
            "12312312312312",
            "Отличное путешествие с замечательными людьми",
            "2026-05-09"
        )
        self.assertIn('title', errors)
         #содержание статьи только цифры
    def test_articles_content_incorrect(self):
        errors = validate_articles(
            "Ладушка67",
            "Поездка по Италии",
            "23423433423434",
            "2026-05-17"
        )
        self.assertIn('content', errors)
        #некорректная дата
    def test_articles_date_incorrect(self):
        errors = validate_articles(
            "Ладушка67",
            "Поездка по Италии",
            "Отличная поездка всем все понравилось",
            "2024-05-09"
        )
        self.assertIn('date', errors)
         #в авторе только цифры
    def test_articles_author_only_digits(self):
        errors = validate_articles(
            "6767676767",
            "Поездка по Италии",
            "Отличная поездка всем все понравилось",
            "2026-05-09"
        )
        self.assertIn('author', errors)
         #в заголовке только цифры
    def test_articles_title_only_digits(self):
        errors = validate_articles(
            "Ладушка6767",
            "6767676767",
            "Отличная поездка всем все понравилось",
            "2026-05-09"
        )
        self.assertIn('title', errors)
         #текст статьи пустой
    def test_articles_content_is_empty(self):
        errors = validate_articles(
            "Ладушка6767",
            "Италия это очень круто!",
            "",
            "2026-05-09"
        )
        self.assertIn('content', errors)
         # короткое имя автора
    def test_articles_short_author(self):
        errors = validate_articles(
            "в",
            "Италия это очень круто!",
            "замечательная страна для путешествий",
            "2026-05-09"
        )
        self.assertIn('author', errors)
         #короткий текст статьи
    def test_articles_short_content(self):
        errors = validate_articles(
            "Дудоня1",
            "Италия это очень круто!",
            "з",
            "2026-05-09"
        )
        self.assertIn('content', errors)
         #автор пустой
    def test_articles_author_empty(self):
        errors = validate_articles(
            "",
            "Путешествие",
            "Длинный текст статьи для проверки",
            "2026-05-09"
        )
        self.assertIn('author', errors)
         #заголовок пустой
    def test_articles_title_empty(self):
        errors = validate_articles(
            "Автор",
            "",
            "Длинный текст статьи для проверки",
            "2026-05-09"
        )
        self.assertIn('title', errors)
         # длинное имя автора
    def test_articles_author_too_long(self):
        errors = validate_articles(
            "А" * 50,
            "Название",
            "Длинный текст статьи для проверки",
            "2026-05-09"
        )
        self.assertIn('author', errors)
         # длинный заголовок статьи
    def test_articles_title_too_long(self):
        errors = validate_articles(
            "Автор",
            "Н" * 150,
            "Длинный текст статьи для проверки",
            "2026-05-09"
        )
        self.assertIn('title', errors)
         #неверный формат даты
    def test_articles_date_invalid_format(self):
        errors = validate_articles(
            "Автор",
            "Название",
            "Длинный текст статьи для проверки",
            "31.12.2025"
        )
        self.assertIn('date', errors)
# =========================================
# ПОЛЬЗОВАТЕЛИ
# =========================================
class TestUsers(unittest.TestCase):
    # Проверка польностью корректных данных пользователя
    def test_users_valid_data(self):
        errors = validate_user(
            "malderdss",
            "dmitrii.kulikov2015@gmail.com",
            "male",
            "5",
            "2026-07-09",
            users=load_users(),
            routes=load_routes()
        )
        self.assertEqual(errors, {})
    
    # Проверка, что 1 email не может принадлежать разным никам
    def test_users_nickname_notequal_email(self):
        errors = validate_user(
            "kosty",
            "dmitrii.kulikov2015@gmail.com",
            "male",
            "5",
            "2026-07-09",
            users=load_users(),
            routes=load_routes()
        )
        # Проверка ошибки email
        self.assertIn('email', errors)
    
    # Проверка, что пользователь не может изменить пол
    def test_users_gender_notequal_user(self):
        errors = validate_user(
            "malderdss",
            "dmitrii.kulikov2015@gmail.com",
            "Женский",
            "5",
            "2026-07-09",
            users=load_users(),
            routes=load_routes()
        )
        # Проверка ошибки пола
        self.assertIn('gender', errors)

    # Проверка некорректных ников
    def test_users_nickname_assertFalse(self):
        list_nickname_uncor = [
            "",
            "1",
            "1kosty",
            "qw--er",
            "!!!.USER",
            "user__",
            "0kosty234",
            "12345"
        ]
        for nickname in list_nickname_uncor:
            self.assertFalse(validation_active_users.validate_nickname(nickname))

    # Проверка корректных ников
    def test_users_nickname_assertTrue(self):
        list_nickname_cor = [
            "kostyKulikov",
            "malderds_",
            "m3BMW",
            "SUAI_college",
            "kosty-kulikov_C326",
            "kosty007"
        ]
        for nickname in list_nickname_cor:
            self.assertTrue(validation_active_users.validate_nickname(nickname))

    # Проверка некорректных email
    def test_users_emails_assertFalse(self):
        list_mail_uncor = [
            "",
            "1",
            "mail@",
            "@mail",
            "kosty@mail",
            "kosty@mail.",
            "@list.ru",
            "kosty.mail.ru",
            "kosty@mail%.ru",
            ".@mail.ru",
            "kosty_@mail.ru"
        ]
        for email in list_mail_uncor:
            self.assertFalse(validation_active_users.validate_email(email))

    # Проверка корректных email
    def test_users_emails_assertTrue(self):
        list_mail_cor = [
            "kulikov@list.ru",
            "andrey20071@mail.com",
            "kosty_kulikov3@gmail.com",
            "user_123@site.net",
            "anna@domain.io",
            "abc100@gmail.com",
            "cont@mail.ru",
            "kulikov07@list.ru",
            "road_loooooooooong3424@gmail.com",
            "email_addres+s@list.ru"
        ]
        for email in list_mail_cor:
            self.assertTrue(validation_active_users.validate_email(email))

    # Проверка некорректного формата даты тура
    def test_users_date_tour_assertFalse(self):
        list_date_ture_uncor = [
            "Две тысячи двадцать шестой-05-15",
            "",
            "2026.06.01",
            "07-05-2026",
            "2026-12_31",
            "1",
            "20-20-20",
            "2026-13-30",
            "2026-01-32",
            "20th-02-30"
        ]
        for tour_date in list_date_ture_uncor:
            self.assertFalse(validation_active_users.validate_tour_date(tour_date))

    # Проверка корректного формата даты тура
    def test_users_date_tour_assertTrue(self):
        list_date_ture_cor = [
            "2026-05-15",
            "2030-12-12",
            "2026-06-01",
            "2027-01-01",
            "2029-9-9",
            "2026-10-10",
            "2027-06-03",
            "2028-09-27",
            "2026-11-23",
            "2027-01-10"
        ]
        for tour_date in list_date_ture_cor:
            self.assertTrue(validation_active_users.validate_tour_date(tour_date))

    # Проверка, что дата тура не должны быть в прошлом
    def test_users_date_tour_before_now_assertFalse(self):
        list_date_ture_uncor = [
            "2025-05-15",
            "2026-05-09",
            "2021-06-01",
            "2024-12-10",
            "2026-04-03",
            "2026-01-01",
            "2012-06-03",
            "2010-09-27",
            "1980-12-25",
            "2021-01-10"
        ]
        for tour_date in list_date_ture_uncor:
            self.assertFalse(validation_active_users.validate_tour_date_after_now(tour_date))

    # Проверка, что дата тура должны быть больше или равна текущей даты
    def test_users_date_tour_after_now_assertTrue(self):
        list_date_ture_cor = [
            "2026-05-12",
            "2030-12-12",
            "2026-06-01",
            "2027-01-01",
            "2029-9-9",
            "2026-10-10",
            "2027-06-03",
            "2028-09-27",
            "2026-11-23",
            "2027-01-10"
        ]
        for tour_date in list_date_ture_cor:
            self.assertTrue(validation_active_users.validate_tour_date_after_now(tour_date))

# Запуск всех тестов
if __name__ == '__main__':
    unittest.main()