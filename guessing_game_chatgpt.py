import random

# Initialize the minimum number of attempts to a very large value
min_attempts = float('inf')

while True:
    # Prompt the player to pick a number between 1 and 10
    print("Welcome to the guessing game! Please pick a number between 1 and 10.")
    player_choice = int(input())
    
    # Generate a random number for the computer's choice
    pc_choice = random.randint(1, 10)
    
    # Initialize attempts counter
    attempts = 1

    # Continue the game until the player's choice matches the computer's choice
    while player_choice != pc_choice:
        if player_choice < pc_choice:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
        
        # Get a new input from the player
        player_choice = int(input())
        
        # Increment the attempts counter
        attempts += 1

    # Update the minimum attempts if the current game had fewer attempts
    if attempts < min_attempts:
        min_attempts = attempts

    # Display a congratulatory message and the number of attempts
    print("Congratulations! You have guessed the number in", attempts, "attempts.")
    print("The minimum number of attempts so far is", min_attempts)
    
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no)")
    
    # If the player enters "no", exit the loop and end the game
    if play_again.lower() == "no":
        break

