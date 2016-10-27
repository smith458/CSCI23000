import random

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
    clearDeck()

    for i in range(5):
        assignCard(PLAYER)
        assignCard(COMP)

    showDeck()
    showHand(PLAYER)
    showHand(COMP)

def clearDeck():
    for i in range(NUMCARDS):
        cardLoc[i] = 0

def assignCard(player):
    while True:
        location = random.randint(0,51)
        if cardLoc[location] == DECK:
            break
    cardLoc[location] = player

def showDeck():
    print(" Location of all Cards")
    print(" #  Card               Location")
    for i in range(NUMCARDS):
        print("%2d  %17s  %6s" % (i, cardName(i), playerName[cardLoc[i]]))
        
def cardName(loc):
    cardname = rankName[loc % 13] + " of " + suitName[int(loc / 13)]
    return cardname

def showHand(player):
    print("\nDiplaying %s hand:" % playerName[player])
    for i in range(NUMCARDS):
        if cardLoc[i] == player:
            print(cardName(i))

main()
