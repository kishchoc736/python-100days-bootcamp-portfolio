import random
from art import logo

def get_card():
    """Selects a random card from a list"""
    list = [11,2,3,4,5,6,7,8,9,10,10,10]
    return random.choice(list)
def add_cards(list, no_of_cards):
    """Adds cards to a list"""
    for i in range(no_of_cards):
        list.append(get_card())

def calculate_score(cards):
    """Calculates the score and handles multiple Aces."""
    score = sum(cards)
    # Natural Blackjack check
    if score == 21 and len(cards) == 2:
        return 0

        # Handle multiple Aces if busting
    while score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare_scores(user_score, computer_score, user_hand, computer_hand):
    """Compares the scores of two lists"""
    if computer_score == 0:
        return "Computer got Blackjack (Natural)! You lose."
    elif computer_score == 21:
        return "Computer got 21, computer wins"
    elif user_score == 0:
        return "You got Blackjack (Natural)! You win!"
    elif user_score == 21:
        return "You got 21, you win"
    elif user_score > 21:
        return "You went over 21, you lose"
    elif computer_score > 21:
        return "Computer went over 21, you win"
    elif user_score == computer_score:
        return "It's a draw"
    elif user_score > computer_score:
        return "You were closer, you win"
    else:
        return "The computer was closer, you lose"


def start_game():
    """Starts the game"""
    print(logo)
    game_over = False
    user_list = []
    computer_list = []

    add_cards(user_list, 2)
    user_score = calculate_score(user_list)
    add_cards(computer_list, 2)
    computer_score = calculate_score(computer_list)

    """ 
    Redundant check:
    
    if user_score == 21 or computer_score == 21:
        game_over = True
    elif user_score > 21 or computer_score > 21:
        game_over = True
    """

    while not game_over:
        user_score = calculate_score(user_list)
        computer_score = calculate_score(computer_list)

        print(f"Your cards: {user_list}, current score: {user_score}")
        print(f"Computer's first card: {computer_list[0]}")

        if user_score > 21 or user_score == 0 or computer_score > 21:
            game_over = True
        else:
            should_draw = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_draw == 'y':
                add_cards(user_list, 1)
            else:
                game_over = True
                while computer_score != 0 and computer_score < 17:
                    add_cards(computer_list, 1)
                    computer_score = calculate_score(computer_list)

    # Final results
    print(f"Your final hand: {user_list}, final score: {user_score}")
    print(f"Computer's final hand: {computer_list}, final score: {computer_score}")

    print(compare_scores(user_score, computer_score, user_list, computer_list))

    #Check status
    # print(compare_scores(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    start_game()