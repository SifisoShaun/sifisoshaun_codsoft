import unittest
from password import *

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        for length in range(4, 21, 4):
            password = generate_password(length)
            self.assertEqual(len(password), length)

    def test_generate_password_characters(self):
        password = generate_password(10)
        for char in password:
            self.assertIn(char, string.ascii_letters + string.digits + string.punctuation)

if __name__ == "__main__":
    unittest.main()
