import random

def display_welcome_message():
    print("Welcome to Rock, Paper, Scissors Game!")

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'You win!'
    else:
        return 'Computer wins!'

def display_result(player_choice, computer_choice, result):
    print(f"Your choice: {player_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    print(result)

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        display_welcome_message()
        player_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, result)
        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1
        print(f"Score - You: {user_score}  Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()

