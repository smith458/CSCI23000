import random

NUMCARDS = 52
NUMSUITS = 4
NUMRANKS = 13
DECK = 0
PLAYER = 1
COMP = 2

playerDeck = [0] * NUMCARDS
compDeck = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
suitU = ("\u2665", "\u2666", "\u2660", "\u2663")
rankName = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
            "Nine", "Ten", "Jack", "Queen", "King", "Ace")
rankAbr = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
playerName = ("deck", "player", "computer")

def main():
    print("Welcome to War!")
    clearDeck()
    dealCards()
    while (max(playerDeck) > 0) and (max(compDeck) > 0):
        incrementDecks()
        displayCount()
        draw(0)
    if max(playerDeck) > 0:
        print("Congratulations! You Win!")
    else:
        print("I win!")

    while True:
        answer = input("\nWould you like to play again, (y)es or (n)o?\n")
        if answer.upper() == "Y":
            main()
        elif answer.upper() == "N":
            print("\n\nBye!!\n\n")
            break

#Clears the contents of both the Player's and User's Deck
def clearDeck():
    for i in range(NUMCARDS):
        playerDeck[i] = 0
        compDeck[i] = 0

#Every card is assigned to the Player's deck or Computer's Deck.
#The value in the List is the order in wich they are located in the deck
def dealCards():
    print("\nDealing.....")
    for i in range(NUMCARDS):
        while True:
            card = random.randint(0,51)
            if playerDeck[card] == DECK and compDeck[card] == DECK:
                break
        if ((i % 2) == 0):
            playerDeck[card] = max(playerDeck) + 1
        if ((i % 2) == 1):
            compDeck[card] = max(compDeck) + 1
    print("Dealt!")
            
#Gives the name of the card based on index in Deck
def cardName(loc):
    name = rankAbr[loc % 13] + suitU[int(loc / 13)]
    return name

#Each player presents a card. They are compared and the
#cards are moved to the back of the winner's Deck
def draw(warCount):
    input("\nPress enter to play a card\n")
    cardCount = 1 + warCount * 2
    playerCard = playerDeck.index(cardCount)
    playerRank = playerCard % 13
    compCard = compDeck.index(cardCount)
    compRank = compCard % 13
    print("Player's   Card: %s" % cardName(playerCard))
    print("Computer's Card: %s" % cardName(compCard))
    
    if playerRank > compRank:
        print("You take the cards!")
        for i in range(1, cardCount + 1):
            playerDeck[playerDeck.index(i)] = max(playerDeck) + 1
            playerDeck[compDeck.index(i)] = max(playerDeck) + 1
            compDeck[compDeck.index(i)] = 0
    elif playerRank < compRank:
        print("I take the cards!")
        for i in range(1, cardCount + 1):
            compDeck[compDeck.index(i)] = max(compDeck) + 1
            compDeck[playerDeck.index(i)] = max(compDeck) + 1
            playerDeck[playerDeck.index(i)] = 0
    else:
        print("War!")
        warCount += 1
        if max(playerDeck) < (1 + warCount * 2):
            for i in range(NUMCARDS):
                playerDeck[i] = 0
        elif max(compDeck) < (1 + warCount * 2):
            for i in range(NUMCARDS):
                compDeck[i] = 0
        else:
            draw(warCount)

#Moves all of the cards forward in both decks
def incrementDecks():
    while playerDeck.count(1) == 0:
        for i in range(NUMCARDS):
            if playerDeck[i] > 0:
                playerDeck[i] -= 1
    while compDeck.count(1) == 0:
        for i in range(NUMCARDS):
            if compDeck[i] > 0:
                compDeck[i] -= 1

#Displays the number of cards in each deck
def displayCount():
    playerCards = NUMCARDS - playerDeck.count(0)
    compCards = NUMCARDS - compDeck.count(0)
    print("\nDeck Card Count")
    print("Player:   %d" % playerCards)
    print("Computer: %d" % compCards)

main()

