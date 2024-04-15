import unittest
from unittest.mock import patch
import io
import sys
import random
from rock_paper_scissor import *

class TestRockPaperScissors(unittest.TestCase):

    @patch('builtins.input', side_effect=['rock'])
    def test_get_user_choice_rock(self, mock_input):
        self.assertEqual(get_user_choice(), 'rock')

    @patch('builtins.input', side_effect=['paper'])
    def test_get_user_choice_paper(self, mock_input):
        self.assertEqual(get_user_choice(), 'paper')

    @patch('builtins.input', side_effect=['scissors'])
    def test_get_user_choice_scissors(self, mock_input):
        self.assertEqual(get_user_choice(), 'scissors')

    @patch('random.choice', return_value='rock')
    def test_get_computer_choice_rock(self, mock_random):
        self.assertEqual(get_computer_choice(), 'rock')

    @patch('random.choice', return_value='paper')
    def test_get_computer_choice_paper(self, mock_random):
        self.assertEqual(get_computer_choice(), 'paper')

    @patch('random.choice', return_value='scissors')
    def test_get_computer_choice_scissors(self, mock_random):
        self.assertEqual(get_computer_choice(), 'scissors')

    def test_determine_winner_player_win(self):
        self.assertEqual(determine_winner('rock', 'scissors'), 'You win!')
        self.assertEqual(determine_winner('paper', 'rock'), 'You win!')
        self.assertEqual(determine_winner('scissors', 'paper'), 'You win!')

    def test_determine_winner_computer_win(self):
        self.assertEqual(determine_winner('scissors', 'rock'), 'Computer wins!')
        self.assertEqual(determine_winner('rock', 'paper'), 'Computer wins!')
        self.assertEqual(determine_winner('paper', 'scissors'), 'Computer wins!')

    def test_determine_winner_tie(self):
        self.assertEqual(determine_winner('rock', 'rock'), 'It\'s a tie!')
        self.assertEqual(determine_winner('paper', 'paper'), 'It\'s a tie!')
        self.assertEqual(determine_winner('scissors', 'scissors'), 'It\'s a tie!')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_result(self, mock_stdout):
        display_result('rock', 'scissors', 'You win!')
        self.assertEqual(mock_stdout.getvalue().strip(), 'Your choice: Rock\nComputer\'s choice: Scissors\nYou win!')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_welcome_message(self, mock_stdout):
        display_welcome_message()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Welcome to Rock, Paper, Scissors Game!')


if __name__ == '__main__':
    unittest.main()
