# Imports
from random import randint, random
import database
from os import system

# Lists with the Suits and the Cards
Suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
Cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Full card deck
deck = []
playerbase = []
# Function to create the cards
def create_cards():
    for suit in Suits:
        for card in Cards:
            deck.append(suit + " " + card)

def clear_deck():
    deck.clear()
    print("The deck has been cleared and ready for new game!")

def main():
    print("Welcome to the king cup game!")
    player_count = input("How many players are participating?: ")

    for i in range(player_count):
        print("What are the name of the players?")
        player_name = input(": ")
        database.insert_name(player_name)
        database.insert_score(player_name, 0)
        playerbase.append(player_name)
        os.system("cls")

    print("These are the players", *playerbase)
    print("let's play!")
    random.shuffle(playerbase)
    