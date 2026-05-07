import unittest

# импорт валидации для пользователей
from files_active_users import validation_active_users
from files_active_users.validation_active_users import validate_user
from files_active_users.storage_active_users import load_users, load_routes

# импорт валидации для новинок
from files_new_items.validation_new_items import validate_route

class Test_test_all(unittest.TestCase):
    #----------------------------
    # Тесты для страницы "Новинки"
    #----------------------------
    # корректные данные — ошибок быть не должно
    def test_items_valid_data(self):
        errors = validate_route(
            "Маршрут 1",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertEqual(errors, {})

    # пустое название маршрута
    def test_items_empty_name(self):
        errors = validate_route(
            "",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('route_name', errors)

    # слишком короткое описание
    def test_items_short_description(self):
        errors = validate_route(
            "Маршрут",
            "Коротко",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('description', errors)

    # неверная дата - не указано время
    def test_items_invalid_date(self):
        errors = validate_route(
            "Маршрут",
            "Хорошее описание маршрута",
            "06-05-2026",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('date', errors)

    # неверная дата - время указано в неверном формате
    def test_items_invalid_time(self):
        errors = validate_route(
            "Маршрут",
            "Хорошее описание маршрута",
            "2026-06-05 20",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('date', errors)

    # одинаковые города подряд
    def test_items_same_cities(self):
        errors = validate_route(
            "Маршрут",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Рим", "Милан"
        )
        self.assertIn('cities', errors)

    # в названии только числа
    def test_items_name_only_digits(self):
        errors = validate_route(
            "12345",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('route_name', errors)

    # в описании только цифры
    def test_items_description_only_digits(self):
        errors = validate_route(
            "Маршрут 1",
            "1234567890",
            "2026-05-06 12:00",
            "Рим", "Флоренция", "Милан"
        )
        self.assertIn('description', errors)

        # английские буквы в названии
    def test_items_name_with_latin(self):
        errors = validate_route(
             "Route 1",
             "Хорошее описание маршрута",
             "2026-05-06 12:00",
             "Рим", "Флоренция", "Милан"
        )
        self.assertIn('route_name', errors)


        # английские буквы в описании
    def test_items_description_with_latin(self):
        errors = validate_route(
              "Маршрут 1",
              "Nice trip in Italy",
              "2026-05-06 12:00",
              "Рим", "Флоренция", "Милан"
        )
        self.assertIn('description', errors)

    #----------------------------
    # Тесты для страницы "Бронирование"
    #----------------------------
    # Корректные данные — ошибок быть не должно
    def test_users_valid_data(self):
        errors = validate_route(
            "maderdss",
            "dmitrii.kulikov2015@gmail.com",
            "Мужской",
            "5",
            "2026-07-09 10:30",
            users = load_users(),
            routes = load_routes())
        self.assertEqual(errors, {})

    # У почты может быть только 1 ник пользователя
    def test_users_nickname_notequal_email(self):
        errors = validate_route(
            "kosty",
            "dmitrii.kulikov2015@gmail.com",
            "Мужской",
            "5",
            "2026-07-09 10:30",
            users = load_users(),
            routes = load_routes())
        self.assertIn('email', errors)

    # Проверка некорректных почт
    def test_users_emails_assertFalse(self):
        list_mail_uncor = [
            "",
            "1",
            "mail@",
            "@mail",
            "kosty@mail",
            "kosty@mail.",
            "kosty@mail.r",
            "kosty@m.ru",
            "@list.ru",
            "kosty.ru",
            "kosty.mail.ru",
            "kosty@mail%.ru",
            ".@mail.ru"
            ]
        # Цикл для проверки каждого email
        for email in list_mail_uncor:
            self.assertFalse(validation_active_users.validate_email(email), f"Email: {email} должен быть неверным")

    # Проверка корректных почт
    def test_users_emails_assertTrue(self):
        list_mail_cor = [
            "kulikov@list.ru",
            "andrey20071@mail.com",
            "kosty_kulikov3@gmail.com",
            "user_123%@site.net",
            "anna@domain.io",
            "abc100@gmail.com",
            "cont@mail.ru",
            "kulikov07@list.ru",
            "road_loooooooooong3424@gmail.com",
            "email_address%+-@list.ru"
         ]
        # Цикл для проверки каждого email
        for email in list_mail_cor:
            self.assertTrue(validation_active_users.validate_email(email), f"Email: {email} должен быть верным")


    # Проверка соответствия некорректных даты_тура по формату ГГГГ-ММ-ДД ЧЧ:ММ
    def test_users_date_tour_assertFalse(self):
        list_date_ture_cor = [
            "Две тысячи двадцать шестой-05-15 5:30",
            "",
            "2026.06.01 23:59",
            "07-05-2026 20:00",
            "2026-12-31 23:00:00"
            ]
        # Цикл для проверки корректной даты тура
        for tour_date in list_date_ture_cor:
            self.assertFalse(validation_active_users.validate_tour_date(tour_date), f"Дата тура: {tour_date} должен быть неверным")

    # Проверка соответствия корректных даты_тура по формату ГГГГ-ММ-ДД ЧЧ:ММ
    def test_users_date_tour_assertTrue(self):
        list_date_ture_cor = [
            "2026-05-15 5:30",
            "2030-12-12 12:00",
            "2026-06-01 23:59",
            "2027-01-01 0:01",
            "2026-12-31 23:00"
            ]
        # Цикл для проверки корректной даты тура
        for tour_date in list_date_ture_cor:
            self.assertTrue(validation_active_users.validate_tour_date(tour_date), f"Дата тура: {tour_date} должен быть верным")

if __name__ == '__main__':
    unittest.main()