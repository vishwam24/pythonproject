# Importing the 'random' module to generate random numbers
import random

# Defining a function 'guess' that takes a parameter 'x'
def guess(x):
    # Generating a random number between 1 and 'x'
    random_number = random.randint(1, x)
    
    # Initializing the variable 'guess' to 0
    guess = 0

    # Starting a loop that continues until the user's guess matches the random number
    while guess != random_number:
        # Asking the user to input a number between 1 and 'x'
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        # Checking if the guessed number is lower than the random number
        if guess < random_number:
            # Printing a message indicating that the guess is too low
            print("Sorry! Guess again. Too low!")
        # Checking if the guessed number is higher than the random number
        elif guess > random_number:
            # Printing a message indicating that the guess is too high
            print("Sorry! Guess again. Too high!")

    # Printing a congratulatory message when the correct number is guessed
    print(f'Yah! Congratulations! You have guessed the number {random_number}')

# Calling the 'guess' function with an argument '10' to guess a number between 1 and 10
guess(10)
