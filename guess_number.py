
# Import the random module
import random

# Initialize an empty list to store attempts for high scores
attempts_list = []

# Define a function to show the current high score
def show_score():
    if not attempts_list:
        print("There is currently no high score, start playing.")
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")

# Initialize variables for attempts and a random number to guess
attempts = 0
rand_number = random.randint(1000, 9999)

# Welcome message and ask for the player's name
print("Hello player! Welcome to the guessing game!")
player_name = input("What is your name? ")

# Ask if the player wants to play
wanna_play = input(f"Hi, {player_name}, would you like to play the guessing game? (Enter Yes/No): ").lower()

# If the player doesn't want to play, exit
if wanna_play == "no":
    print("That's cool, Thanks!")
    exit()
else:
    show_score()

# Main game loop
while wanna_play == "yes":
    try:
        # Get a guess from the player
        guess = int(input("Pick a number between 1000 and 9999: "))

        # Check if the guess is within the given range
        if guess < 1000 or guess > 9999:
            raise ValueError("Please guess a number within the given range.")

        # Increment the attempts
        attempts += 1

        # Check if the guess is correct
        if guess == rand_number:
            print("Nice, you got it!")
            print(f"It took you {attempts} attempts.")
            wanna_play = input("Would you like to play again? (Enter Yes/No): ").lower()

            # Update high score list
            attempts_list.append(attempts)

            if wanna_play == "no":
                print("That's cool, have a good day.")
            else:
                attempts = 0
                rand_number = random.randint(1000, 9999)
                show_score()
                continue
        elif guess > rand_number:
            print("It is lower!")
        else:
            print("It is higher!")
    except ValueError as err:
        print(err)
