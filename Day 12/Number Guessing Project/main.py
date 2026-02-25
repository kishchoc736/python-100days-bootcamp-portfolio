from random import randint
import art

def guessing_game():
    print(art.logo)
    print(f"Welcome to Number Guessing Game! \nI'm thinking of a number between 1 and 100.\n")
    difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    guess_check = False
    no_of_guesses = 0
    secret_number = randint(1, 100)
    if difficulty == "easy":
        no_of_guesses = 10
    elif difficulty == "hard":
        no_of_guesses = 5

    while not guess_check and no_of_guesses != 0:
        print(f"You have {no_of_guesses} guesses left.")
        guess = int(input("Make a guess: "))
        if guess == secret_number:
            guess_check = True
            print(f"You got it, the secret number was {secret_number}")
        else:
            no_of_guesses -=1
            if guess < secret_number:
                print(f"Too low.")
            elif guess > secret_number:
                print(f"Too high.")
            if no_of_guesses > 0:
                print("Guess again.")
    if no_of_guesses == 0:
        print("You've run out of guesses. Rerun to play again")
guessing_game()




