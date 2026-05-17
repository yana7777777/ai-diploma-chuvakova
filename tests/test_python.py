import unittest
import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from main import build_project_report
from text_utils import normalize_text, word_count, contains_word
from data_utils import find_by_name, filter_by_value, count_items
from file_utils import save_text, load_text, append_text, count_lines
from json_utils import save_json, load_json, dict_to_json_text


class TestTextProcessing(unittest.TestCase):
    """Тестирование обработки текста"""
    
    def test_normalize_text(self):
        """Проверка нормализации текста (убирает пробелы, приводит к нижнему регистру)"""
        result = normalize_text("   ПРИВЕТ МИР   ")
        self.assertEqual(result, "привет мир")
    
    def test_normalize_text_with_punctuation(self):
        """Проверка нормализации текста со знаками препинания"""
        result = normalize_text("Привет, Мир!")
        self.assertEqual(result, "привет, мир!")
    
    def test_word_count(self):
        """Проверка подсчёта слов"""
        result = word_count("один два три три")
        self.assertEqual(result, 4)
    
    def test_word_count_empty(self):
        """Проверка подсчёта слов в пустой строке"""
        result = word_count("")
        self.assertEqual(result, 0)
    
    def test_contains_word_true(self):
        """Проверка, что слово найдено в тексте"""
        result = contains_word("я люблю python программирование", "python")
        self.assertTrue(result)
    
    def test_contains_word_false(self):
        """Проверка, что слово не найдено в тексте"""
        result = contains_word("я люблю python программирование", "java")
        self.assertFalse(result)
    
    def test_contains_word_case_insensitive(self):
        """Проверка, что регистр не влияет на поиск"""
        result = contains_word("Python программирование", "python")
        self.assertTrue(result)


class TestDataProcessing(unittest.TestCase):
    """Тестирование обработки данных (списки пользователей)"""
    
    def setUp(self):
        self.users = [
            {"id": 1, "name": "Иван", "city": "Самара", "age": 40},
            {"id": 2, "name": "Соня", "city": "Москва", "age": 30},
            {"id": 3, "name": "Игорь", "city": "Казань", "age": 50},
            {"id": 4, "name": "Стас", "city": "Самара", "age": 58},
        ]
    
    def test_find_by_name(self):
        """Поиск существующего пользователя по имени"""
        found = find_by_name(self.users, "Иван")
        self.assertIsNotNone(found)
        self.assertEqual(found["name"], "Иван")
        self.assertEqual(found["city"], "Самара")
    
    def test_find_by_name_not_exists(self):
        """Поиск несуществующего пользователя"""
        found = find_by_name(self.users, "Пётр")
        self.assertIsNone(found)
    
    def test_filter_by_value(self):
        """Фильтрация пользователей по городу"""
        samara_users = filter_by_value(self.users, "city", "Самара")
        self.assertEqual(len(samara_users), 2)
        for user in samara_users:
            self.assertEqual(user["city"], "Самара")
    
    def test_filter_by_value_no_matches(self):
        """Фильтрация без совпадений"""
        result = filter_by_value(self.users, "city", "Лондон")
        self.assertEqual(len(result), 0)
    
    def test_count_items(self):
        """Подсчёт количества элементов в списке"""
        self.assertEqual(count_items(self.users), 4)
        self.assertEqual(count_items([]), 0)


class TestFileOperations(unittest.TestCase):
    """Тестирование файловых операций"""
    
    def setUp(self):
        self.test_filename = "test_temp.txt"
    
    def tearDown(self):
        # Удаляем тестовый файл после каждого теста
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
    
    def test_save_and_load_text(self):
        """Сохранение и загрузка текстового файла"""
        content = "Тестовое содержимое"
        save_text(self.test_filename, content)
        loaded = load_text(self.test_filename)
        self.assertEqual(loaded, content)
    
    def test_append_text(self):
        """Добавление текста в существующий файл"""
        save_text(self.test_filename, "Первая строка\n")
        append_text(self.test_filename, "Вторая строка")
        content = load_text(self.test_filename)
        self.assertIn("Первая строка", content)
        self.assertIn("Вторая строка", content)
    
    def test_count_lines(self):
        """Подсчёт строк в файле"""
        save_text(self.test_filename, "строка1\nстрока2\nстрока3")
        self.assertEqual(count_lines(self.test_filename), 3)


class TestJSONOperations(unittest.TestCase):
    """Тестирование операций с JSON"""
    
    def setUp(self):
        self.test_filename = "test_config.json"
    
    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
    
    def test_save_and_load_json(self):
        """Сохранение и загрузка JSON файла"""
        data = {"name": "Тест", "value": 100, "items": [1, 2, 3]}
        save_json(self.test_filename, data)
        loaded = load_json(self.test_filename)
        self.assertEqual(loaded, data)
    
    def test_dict_to_json_text(self):
        """Преобразование словаря в JSON-строку"""
        data = {"key": "value", "number": 42}
        json_str = dict_to_json_text(data)
        # Проверяем, что это валидный JSON
        parsed = json.loads(json_str)
        self.assertEqual(parsed, data)


class TestBuildReport(unittest.TestCase):
    """Тестирование функции build_project_report"""
    
    def test_build_report_returns_dict(self):
        """Проверка, что функция возвращает словарь"""
        text = "   test   "
        tasks = ["task1"]
        users = [{"name": "user1"}]
        
        report = build_project_report(text, tasks, users)
        self.assertIsInstance(report, dict)
    
    def test_build_report_correct_counts(self):
        """Проверка правильности подсчётов"""
        text = "один два три"
        tasks = ["t1", "t2", "t3", "t4"]
        users = ["u1", "u2"]
        
        report = build_project_report(text, tasks, users)
        self.assertEqual(report["task_count"], 4)
        self.assertEqual(report["users_count"], 2)
    
    def test_build_report_has_all_keys(self):
        """Проверка наличия всех ключей в отчёте"""
        report = build_project_report("text", ["task"], [{"name": "user"}])
        expected_keys = ["clean_text", "word_count", "has_python", "task_count", "users_count"]
        for key in expected_keys:
            self.assertIn(key, report)


if __name__ == "__main__":
    unittest.main()