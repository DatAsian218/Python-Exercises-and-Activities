"""
    Alexandra Triampol
    7/26/16

    Enter # of Players
    Dealer gives 2 cards to himself and the # of Players
    Make point count of the 2 cards available

    Ace equals 1 or 11
    IF PlayerTotal is LESS THAN or EQUAL to 10
        - Ace = 11
    else
        - Ace = 1

    Ask Player if they want to hit or stand
    IF hit:
        - give Player another card
        - make new point total
    IF stand:
        - do nothing to Player
        - ask next player

    Loop through # of Players there are
    Compare all point totals to Dealer
    IF PlayerTotal EQUALS Dealer
        - win
    else
        - lose
    IF PlayerTotal is GREATER THAN 21
        - lose

    END



"""
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
        "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
        "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
        "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", ]

import random

class Card(object):
    def makePlayerPoints(self, playerCard1, playerCard2):
        points = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

        pointSet1 = points[playerCard1]
        pointSet2 = points[playerCard2]
        playerPoints = pointSet1 + pointSet2

        if (((playerCard1 == "A") or (playerCard2 == "A")) and (playerPoints == 11)):
            playerPoints = playerPoints + 10
        elif ((playerCard1 == "A") and (playerCard2 == "A")):
            playerPoints = 2

        return playerPoints

    def makeDealerPoints(self, dealerCard1, dealerCard2):
        points = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

        pointSet1 = points[dealerCard1]
        pointSet2 = points[dealerCard2]
        dealerPoints = pointSet1 + pointSet2

        if ((dealerCard1 == "A") or (dealerCard2 == "A")) and (dealerPoints == 11):
            dealerPoints = dealerPoints + 10
        elif ((dealerCard1 == "A") and (dealerCard2 == "A")):
            dealerPoints = 2

        return dealerPoints

    def hitPlayer(self,playerDrawsCard,pScoreList,playerNum):
        points = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

        addPoints = points[playerDrawsCard]
        currentPoints = pScoreList[playerNum]
        newPoints = addPoints+currentPoints

        if ((playerDrawsCard == "A") and (currentPoints < 10)):
            newPoints = newPoints + 10
        else:
            newPoints = newPoints

        return newPoints

    def hitDealer(self,dealerDrawsCard,dealerStartPoints):
        points = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

        addPoints = points[dealerDrawsCard]
        newPoints = addPoints + dealerStartPoints

        if ((dealerDrawsCard == "A") and (newPoints < 10)):
            newPoints = newPoints + 10
        else:
            newPoints = newPoints

        return newPoints


class Deck(object):
    def passCard(self, deck):
        card = random.choice(deck)
        deck.remove(card)
        return card
        pass


class Player(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    pass


class Dealer(Player):
    pass


class Blackjack(object):
    pass



def main():
    deckOfCards = Deck()
    pointCard = Card()


    dealer = Dealer("Dealer")
    dealerCard1 = deckOfCards.passCard(deck)
    dealerCard2 = deckOfCards.passCard(deck)
    dealerStartPoints = pointCard.makeDealerPoints(dealerCard1, dealerCard2)


    numOfPlayers = int(input("How many players? (No more than 6): "))

    print()

    if (numOfPlayers >6):
        print("You can't play with more than 6 people.")
        print()
        numOfPlayers = int(input("How many players? (No more than 6): "))

    print()

    playerList = []
    pScoreList = []
    pCardList = []



    for i in range(numOfPlayers):
        player = Player("Player")
        playerList.append(player)

    for playerNum in range(numOfPlayers):
        playerCard1 = deckOfCards.passCard(deck)
        playerCard2 = deckOfCards.passCard(deck)
        playerStartPoints = pointCard.makePlayerPoints(playerCard1, playerCard2)
        pScoreList.append(playerStartPoints)
        pCardList.append(playerCard1+" "+playerCard2+" ")

        print(str(playerList[playerNum]), str(playerNum + 1) + ":",
              str(pCardList[playerNum])+"-",str(pScoreList[playerNum]), "points")

    print(str(dealer) + ":", str(dealerCard1), str(dealerCard2), "-", str(dealerStartPoints), "points")

    for i in range(numOfPlayers):
        count = 0
        player = 1
        response = str(input("Player " + str(player) + "," + " do you want to hit or stand? [h / s]: "))
        if (response == "h"):
            playerDrawsCard = deckOfCards.passCard(deck)
            previousCards = pCardList[count]

            pCardList.insert(count, previousCards + playerDrawsCard + " ")

            newPoints = pointCard.hitPlayer(playerDrawsCard, pScoreList, count)

            pScoreList.insert(count, newPoints)

            print(str(playerList[count]), str(count + 1) + ":", str(pCardList[count]) + "-",
                  str(pScoreList[count]), "points")

            if (pScoreList[count] > 21):
                print("'Looks like you went over 21.'")
                break
        while response == "s":
            if (response == "s"):
                count += 1
                player += 1
                break



main()