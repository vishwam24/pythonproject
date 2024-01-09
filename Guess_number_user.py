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
    

# Defining a function 'computer_guess' that takes an argument 'x'   
def coumputer_guess (x):
    # Initializing the variable 'low' to 1
    low = 1

    # Initializing the variable 'high' to the value of 'x'
    high = x

    # Initializing the variable 'feedback' to an empty string
    feedback = ''

    # Starting a while loop that continues until the user inputs 'c' for correct
    while feedback != 'c' :

         # Checking if 'low' is not equal to 'high'
        if low != high:

            # Generating a random guess between 'low' and 'high'
            guess = random.randint(low,high)

        else:

            # Assigning 'guess' to 'low' when 'low' equals 'high' (the last possible guess)
            # Note: Comment suggests it could be 'high' as well because 'low' equals 'high'
            guess = low # could be high b/c low = high

        # Asking the user for feedback on the guess: too high, too low, or correct    
        feedback = input(f'Is {guess} too high (H), too low(L), or Correct (c)??').lower()

        # Checking if the feedback is 'h' for too high
        if feedback =='h':
             # Updating 'high' to be one less than the guess
            high = guess - 1

        # Checking if the feedback is 'l' for too low
        elif feedback == 'l':
            # Updating 'low' to be one more than the guess
            low = guess + 1


    # Printing a message indicating the computer guessed the user's number correctly
    print (f'Yah ! The cpmputer guessed your number,  {guess}, correctly !')

coumputer_guess(1000)
