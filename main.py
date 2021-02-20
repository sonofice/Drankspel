#imports
import random

# Suits dictionary 
suits = {
    0: 'Clubs',
    1: 'Diamonds',
    2: 'Hearts',
    3: 'Spades'
}

# Cards dictionary
cards = {
    0: 'Ace',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'Jack',
    11: 'Queen',
    12: 'King'
}

def draw_cards(num_of_cards, list_dealt=[]):
    for z in range(num_of_cards):
        x = randint(0,3)
        y = randint(0,12)
        mycard = "{0} of {1}".format(cards[y],suits[x])
        if mycard not in list_dealt:
            list_dealt.append(mycard)
        else:
            num_of_cards = num_of_cards - z
            return draw_cards(num_of_cards,list_dealt)
            
    return list_dealt

# start of script
# Enter number of cards the player wants to get from the deck
default = 1
mydraw = draw_cards(input("How many cards do you want to draw?: ")) #call the function with the number of cards you want. 
if not input:
    mydraw = default

i = 0
for x in mydraw:
    i += 1
    if i == len(mydraw):
        print("...And your last card is the {0}".format(str(x)))
    else:
        print("You got the {0}".format(str(x)))
