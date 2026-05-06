import unittest
from files_new_items.validation_new_items import validate_route

class Test_test_all(unittest.TestCase):
    # Тесты для страницы "Новинки"
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

    def test_items_same_cities(self):
        errors = validate_route(
            "Маршрут",
            "Хорошее описание маршрута",
            "2026-05-06 12:00",
            "Рим", "Рим", "Милан"
        )
        self.assertIn('cities', errors)

if __name__ == '__main__':
    unittest.main()
