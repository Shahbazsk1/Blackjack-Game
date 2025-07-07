import random
import art



def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_choice = random.choice(cards)
    return cards_choice

def calculate_score(cards):
    if sum(cards) ==21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_scores, computer_scores):
    if user_scores == computer_scores:
        return "Draw🙃"
    elif computer_scores == 0:
        return "Lose! Opponent has Blackjack😱"
    elif user_scores == 0:
        return "Win! With A Blackjack😎"
    elif user_scores > 21:
        return "You went Over, You Loss😭"
    elif computer_scores > 21:
        return "Opponent went over, You win😁"
    elif user_scores > computer_scores:
        return "You Win😄"
    else:
        return "You Loss😤"

def play_game():
    print(art.logo)
    user_card = []
    computer_card =[]
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, Current score {user_score}")
        print(f"computer's First Cards: {computer_card[0]}")

        if user_score == 0 and computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_input = input("Type 'y' to get another cards, Type 'n' to pass: ")
            if user_input == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score <17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"Your Final Hand:{user_card}, Final Score: {user_score}")
    print(f"Computer Final Hand: {computer_card}, Final Score: {computer_score}")
    print(compare(user_score,computer_score ))

while input("Do you want to play a game of Blackjack? Type 'y', Type 'n': ") == 'y':
    print("\n" * 3)
    play_game()