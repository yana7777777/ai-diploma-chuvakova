import unittest
import sys
import os

# Добавляем папку src в путь поиска
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from main import build_project_report


class TestFinanceCSV(unittest.TestCase):
    """Тестирование нового финансового CSV функционала"""

    def setUp(self):
        self.test_text = "   Тестовый проект   "
        self.test_tasks = ["задача1", "задача2"]
        self.test_users = [
            {"id": 1, "name": "Анна", "city": "Москва"},
            {"id": 2, "name": "Иван", "city": "Самара"}
        ]

    def test_report_structure(self):
        report = build_project_report(self.test_text, self.test_tasks, self.test_users)
        expected_keys = ["clean_text", "word_count", "has_python", "task_count", "users_count"]
        for key in expected_keys:
            self.assertIn(key, report)


if __name__ == "__main__":
    unittest.main()