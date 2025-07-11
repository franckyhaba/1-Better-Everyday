import random  # import the random module

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Welcome message
print("\nWelcome to Francky's Guessing Game!\n")

# Start the guessing loop
while True:
    try:
        # Ask for a guess every time
        guessingNum = int(input("Guess the correct number to win (1-10): "))
        
        # Check if the guess is correct
        if guessingNum == secret_number:
            print("You have guessed correctly! You win!!")
            break  # Exit the loop when guessed right

        elif guessingNum < secret_number:
            print("Your guess was too low, try again!\n")

        else:  # guessingNum > secret_number
            print("Your guess was too high, try again!\n")

    except ValueError:
        # If user types something that can't be turned into a number
        print("Invalid input. Please enter a number between 1 and 10.\n")

