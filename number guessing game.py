import random

def number_guessing_game():

    target_number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < target_number:
            print("Too low! Try a higher number.")
        elif user_guess > target_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number ({target_number}) correctly!")
            return

        attempts -= 1

    print(f"Sorry, you've run out of attempts. The number was {target_number}. Better luck next time!")


number_guessing_game()
