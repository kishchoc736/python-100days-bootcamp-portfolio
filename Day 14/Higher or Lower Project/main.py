import random
import game_data
import art


def display_art():
    print(art.logo)


def get_new_account(account_a):
    """
    Helps get an account_b based on account_a
    """
    account_b = random.choice(game_data.data)

    #prevent the same account or equal follower counts
    while (
        account_b == account_a
        or account_b["follower_count"] == account_a["follower_count"]
    ):
        account_b = random.choice(game_data.data)

    return account_b

def game():
    score = 0
    should_continue = True
    account_a = random.choice(game_data.data)
    account_b = get_new_account(account_a)

    display_art()

    while should_continue:
        print(f"Compare A: {account_a['name']}, B: {account_b['name']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        # refine code to decide correct answer and check only once
        if account_a["follower_count"] > account_b["follower_count"]:
            correct_answer = "A"
        else:
            correct_answer = "B"

        if choice not in ["A", "B"]:
            print("You have entered an invalid choice, please enter 'A' or 'B'")
            continue

        if choice == correct_answer:
            score += 1
            print(f"Correct Answer! Your score is {score}.\n")

            account_a = account_b
            account_b = get_new_account(account_a)

        else:
            print("You lost!")
            should_continue = False

game()