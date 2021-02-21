# Imports
from random import randint


# Lists with the Suits and the Cards
Suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
Cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Full card deck
deck = []

# Function to create the cards
def create_cards():
    for suit in Suits:
        for card in Cards:
            deck.append([suit + " " + card])
create_cards()
print(*deck)



