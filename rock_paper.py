import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")  # Taking user input
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    # Check if the user wins using the is_win function
    if is_win(user, computer):
        return 'You Won!'

    return 'You Lost'

# Define the is_win function outside the play function
def is_win(player, opponent):
    # Return true if the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False  # Return false if the player doesn't win

# Call the play function to start the game
result = play()
print(result)  # Print the result of the game

