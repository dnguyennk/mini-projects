import random
from art import logo

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculate Score
def calculateScore(cards):
    """Take the cards and calculate the score"""
    # Case 1: Ace + 10 (Blackjack)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Case 2: Score > 21, remove 11 and replace with a 1 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

# Compare scores between the player and computer
def compare(userScore, computerScore):
    if userScore == computerScore:
        return "Draw 🙃"
    elif computerScore == 0:
        return "Oh no you lose 😱"
    elif userScore == 0:
        return "Win win win 🤯"
    elif userScore > 21:
        return "You went over. You lose 😭"
    elif computerScore > 21:
        return "Opponent went over. You win 😎"
    elif userScore > computerScore:
        return "You win 😁"
    else: 
        return "You lose 😤"
    
def play_game():
    # Deal the player and computer 2 cards
    user_cards = []
    computer_cards = []
    isGameOver = False
    
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not isGameOver:
        userScore = calculateScore(user_cards)
        computerScore = calculateScore(computer_cards)
        print(f"    Your cards: {user_cards}, your current score: {userScore}")
        print(f"    Computer's 1st card: {computer_cards[0]}")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else:
            user_continue = input("Type 'y' to get another card, 'n' to pass: ")
            if user_continue == "y":
                user_cards.append(deal_card())
            else:
                isGameOver = True


    # Computer keeps drawing cards as long as it has a score < 17
    while computerScore != 0 and computerScore < 17:
        computer_cards.append(deal_card())
        computerScore = calculateScore(computer_cards)
    print(f"    You final hand: {user_cards}, your final score: {userScore}")
    print(f"    Computer's final hand: {computer_cards}, opponent's final score: {computerScore}")   
    print(compare(userScore, computerScore))

while input("Wanna play again? Type 'y' or 'n': ") == "y":
    print(logo)
    play_game()