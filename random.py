import random
import time

def get_valid_guess():
   
    while True:
        guess = input("Enter your guess (1-200): ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 200:
                return guess
        print("Please enter a valid number between 1 and 200.")

def play_game():
    
    number = random.randint(1, 200)  # Generate random number between 1 and 200
    guesses_taken = 0

    print("Welcome to the Number Guessing Game!")
    name = input("May I ask for your name? ")

    print(f"Hey {name}, I'm thinking of a number between 1 and 200.")
    print("You have 6 attempts to guess it. Let's begin!"
    time.sleep(1)

    while guesses_taken < 6:
        guess = get_valid_guess()
        guesses_taken += 1

        if guess < number:
            print("Too low! Try guessing a higher number.")
        elif guess > number:
            print("Too high! Try guessing a lower number.")
        else:
            print(f"Congratulations, {name}! You guessed the number {number} in {guesses_taken} guesses!")
            return

    print(f"Sorry, {name}. The number I was thinking of was {number}.")

def main():
   
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        play_game()
        play_again = input("Do you want to play again? (yes/no) ")

if __name__ == "__main__":
    main()
