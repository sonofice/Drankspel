# Imports
import random
import database
import os

# Game version
version = 1.0

# Lists with the Suits and the Cards
Suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
Cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Full card deck
deck = []

# List for the player names
playerbase = []

# Creating all cards
def create_cards():
    for suit in Suits:
        for card in Cards:
            deck.append(suit + " " + card)

def shuffle():
    PB_tmp = []
    PB_tmp = playerbase
    random.shuffle(playerbase)
    random.shuffle(deck)
    if playerbase[0] == PB_tmp[0]:
        random.shuffle(playerbase)
        random.shuffle(deck)
    else:
        return

def main():
    print("Welcome to the king cup game!")
    player_count = int(input("How many players are participating?: "))

    # Insert the amount of players into the game
    for i in range(player_count):
        print("What are the name of the players?")
        while True:
            player_name = input(": ")
            if len(player_name) >= 15:
                print("Please fill in a name lower then 15 character")
            else:
                break
        # Insert the user into the DB       
        #database.insert_name(player_name)
        #database.insert_score(player_name, 0)

        # Insert the user into the playerbase list
        playerbase.append(player_name)
        os.system("cls")

    print("These are the players", *playerbase)
    print("let's play!")
    while True:
        # Shuffling the players and the card deck

        random.shuffle(playerbase)
        random.shuffle(deck)

        print("The first player is", playerbase[0], "and gets the card:", deck[0])

        # Creating a temporary list to store the used cards in and the removing of a card out of 
        # the card deck
        tmp_deck = deck.pop(0)

        for k in range(len(deck)):
            input("Press enter for the next round")
            shuffle()
            os.system("cls")
            print("Next is", playerbase[0], "with card", deck[0])
            

        # When no cards exist in the deck, user input if game needs to restart
        print("All cards have been used! This is a sad day...")
        print("Do you want to play again? Yes or No?")
        user_input = input(": ")
        if user_input.lower == "yes" or "y" or "ye":
            print("let's go!")
            os.system("cls")
            create_cards()
        else:
            break

# Start of the script/game
if __name__ == "__main__":
    create_cards()
    main()