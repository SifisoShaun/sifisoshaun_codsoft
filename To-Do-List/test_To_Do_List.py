import unittest
from datetime import datetime
from unittest.mock import patch
from io import StringIO
import os

from To_Do_List import *

class TestToDoListFunctions(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_tasks.txt"
        with open(self.test_file, "w") as file:
            file.write("Task1\nDescription1\n2024-04-20\n---\n")

    def tearDown(self):
        os.remove(self.test_file)

    def test_add_task(self):
        to_do_list = []
        with patch("builtins.input", side_effect=["Task2", "Description2", "2024-04-22"]):
            add_task(to_do_list)
        self.assertEqual(len(to_do_list), 1)
        self.assertEqual(to_do_list[0]["name"], "Task2")

    def test_remove_task(self):
        to_do_list = [{"name": "Task1", "description": "Description1", "due_date": "2024-04-20"}]
        with patch("builtins.input", return_value="Task1"):
            remove_task(to_do_list, "Task1")
        self.assertEqual(len(to_do_list), 0)

    def test_update_task(self):
        to_do_list = [{"name": "Task1", "description": "Description1", "due_date": "2024-04-20"}]
        with patch("builtins.input", side_effect=["Task1", "Updated Task1", "Updated Description1", "2024-04-22"]):
            update_task(to_do_list, "Task1", "Updated Task1", "Updated Description1", "2024-04-22")
        self.assertEqual(to_do_list[0]["name"], "Updated Task1")
        self.assertEqual(to_do_list[0]["description"], "Updated Description1")
        self.assertEqual(to_do_list[0]["due_date"], "2024-04-22")

    def test_display_tasks(self):
        to_do_list = [{"name": "Task1", "description": "Description1", "due_date": "2024-04-20"}]
        with patch("sys.stdout", new=StringIO()) as fake_output:
            display_tasks(to_do_list)
            expected_output = "Task1: Description1 (Due: 2024-04-20)"
            self.assertIn(expected_output, fake_output.getvalue().strip())

    def test_save_to_file(self):
        to_do_list = [{"name": "Task1", "description": "Description1", "due_date": "2024-04-20"}]
        save_to_file(to_do_list, self.test_file)
        with open(self.test_file, "r") as file:
            content = file.read()
            self.assertIn("Task1", content)
            self.assertIn("Description1", content)
            self.assertIn("2024-04-20", content)

    def test_load_tasks_from_file(self):
        to_do_list = load_tasks_from_file(self.test_file)
        self.assertEqual(len(to_do_list), 1)
        self.assertEqual(to_do_list[0]["name"], "Task1")
        self.assertEqual(to_do_list[0]["description"], "Description1")
        self.assertEqual(to_do_list[0]["due_date"], "2024-04-20")

if __name__ == "__main__":
    unittest.main()
