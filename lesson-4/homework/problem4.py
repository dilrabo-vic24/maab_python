import random

def number_guessing_game():

    while True: 
        secret_number = random.randint(1, 100)
        attempts = 0

        while attempts < 10:
            attempts += 1
            guess = int(input(f"Attempt {attempts}: Enter your guess: "))

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("You guessed it right!")
                break 

        if attempts == 10:
            print(f"You lost. The number was {secret_number}.")

        play_again = input("Want to play again? (Y/YES/y/yes/ok): ").lower()
        if play_again not in ['y', 'yes', 'ok']:
            print("Thanks for playing!")
            break

number_guessing_game()