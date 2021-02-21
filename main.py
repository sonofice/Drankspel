# Imports
from random import randint, random
import database
import os

# Lists with the Suits and the Cards
Suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
Cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Full card deck
deck = []

# List for the player names
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

    # Insert the amount of players into the game and DB
    for i in range(player_count):
        print("What are the name of the players?")
        while True:
            player_name = input(int(": "))
            if player_name.count > 15:
                print("Please fill in a name lower then 15 character")
            else:
                break

        database.insert_name(player_name)
        database.insert_score(player_name, 0)
        playerbase.append(player_name)
        os.system("cls")

    print("These are the players", *playerbase)
    print("let's play!")

    # Shuffling the players and the card deck
    random.shuffle(playerbase)
    random.shuffle(deck)

    print("The first player is ", playerbase[0], "and gets the card:", deck[0])
    # Creating a temporary deck to store the used cards in and the removing of a card out of 
    # the card deck
    tmp_deck = []
    tmp_deck = deck.pop(0)


