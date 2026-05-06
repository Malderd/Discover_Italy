import unittest

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
if __name__ == '__main__':
    unittest.main()