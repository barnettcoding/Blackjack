
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = []
computer_hand = []

import random
from art import logo

busted = False
blackjack = False
game_over = False

user_name = {"user": ""}
users_turn = True

for i in range(2):
    user_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
print(logo)

print("Ready to play blackjack? Lets Go!")
user_name["user"] = input("What is your name?")
print (f"The dealer has a {computer_hand[1]}")
print(user_hand)
print (f" Your cards are {user_hand[0]} and {user_hand[1]}")

def calculate_score(player_hand):
    global busted
    global blackjack
    if sum(player_hand) > 21:
        busted = True 
        return sum(player_hand)
    elif sum(player_hand) == 21:
        blackjack = True
        return sum(player_hand)
    else:
        return sum(player_hand)

def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        print("The Game is a Draw!")
    elif user_score > computer_score:
        print(f"You had {user_score}. The computer had {computer_score}. You Win!!!")
    else:
        print(f"You had {user_score}. The computer had {computer_score}. Computer Wins!!!")
    return

while users_turn:
    user_score = calculate_score(user_hand)
    if busted:
        print(f"{user_name['user']}'s score is {user_score}. {user_name['user']} busted!!")
        print(f"The computer had {sum(computer_hand)}. The computer wins")
        game_over = True
        users_turn = False
    elif blackjack:
        print(f"{user_name['user']}'s score is {user_score}. {user_name['user']} got blackjack!!")
        print(f"The computer had {sum(computer_hand)}.")
        game_over = True
        users_turn = False
    else:
        hit_or_stay = input(f"Your cards add up to: {user_score}. Would you like to hit or stay?  ")
        if hit_or_stay == "hit":
            user_hand.append(random.choice(cards))
            print(user_hand)
            calculate_score(user_hand)
        elif hit_or_stay == "stay":
            users_turn = False
            computer_hand.append(random.choice(cards))
            
        else:
            print("invalid response")

while not game_over:
    computer_score = calculate_score(computer_hand)
    if busted:
        print(f"The computer is busted!!")
        print(f"You win!!")
        game_over = True
    elif blackjack:
        print(f"The computer got blackjack!!")
        game_over = True
    elif computer_score < 17 or 11 in computer_hand:
        computer_hand.append(random.choice(cards))
        computer_score = calculate_score(computer_hand)
    else:
        game_over = True
        compare_scores(user_score, computer_score)
