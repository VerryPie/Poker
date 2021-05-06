import random
from collections import Counter
import itertools

Colour = {
    3: 'CLUBS',
    2: 'DIMONDS',
    1: 'HEARTS',
    0: 'SPADES'
}

Figure = {
    14: 'ACE',
    13: 'KING',
    12: 'QUEEN',
    11: 'JACK'
}

Result = {
    9: 'Poker',
    8: 'Four of Kind',
    7: 'Full house',
    6: 'Flush',
    5: 'Straight',
    4: 'Three of kind',
    3: 'Two pair',
    2: 'One pair',
    1: 'High card'

}

def GetResultName(val):
    for key, value in Result.items():
        if val == value:
            return key
    raise Exception("key doesn't exist")

class Card():
    def __init__(self, colour, figure):
        self.colour = colour
        self.figure = figure

    def getFigureName(self):
        if self.figure in range(11, 15):
            return Figure[self.figure]
        return self.figure

    def geColourName(self):
        return Colour[self.colour]

    def __str__(self):
        return f'Card colour is {self.geColourName()} and figure is {self.getFigureName()}'

    def get_colour(self):
        return self.colour

    def get_figure(self):
        return self.figure

    def __lt__(self, other):
        if self.figure < other.figure:
            return True

    def __eq__(self, other):
        if self.figure == other.figure:
            return True

    def __gt__(self, other):
        if self.figure > other.figure:
            return True


class Deck():
    def shuffle(self):
        random.shuffle(self.cardList)

    def __init__(self):
        self.cardList = []
        for col in Colour:
            for num in range(2, 15):
                self.cardList.append(Card(colour=col, figure=num))

        self.shuffle()

    def drawCard(self):
        return self.cardList.pop()

    def __str__(self):
        [print(card) for card in self.cardList]


class Hand():
    def __init__(self, deck, size):
        self.cards = []
        for i in range(size):
            self.cards.append(deck.drawCard())

    def __str__(self):
        hand_cards = ''
        for card in self.cards:
            hand_cards = hand_cards + f' {card.getFigureName()}_{card.geColourName()}'
        return hand_cards



class Player:

    def __init__(self, nick):
        self.avaiable_amount = 1000
        self.name = nick

    def turn(self, play, game):
        if play == 1:
            print("You have finished in this round")
        elif play == 2:
            if self.bet != game.getHighestBet():
                print('You cannot check, you need to raise ammount')
        elif play == 3:
            print('You cannot check, you need to raise ammount')
        elif play == 4:
            gameHighestPossibleAmount = game.getHighestAvaiableAmount()
            if self.avaiable_amount <= gameHighestPossibleAmount:
                print('You playied All in')
            else:
                print('You cannot play all in play raise to: ' + gameHighestPossibleAmount + ' instead')
        elif play == 5:
            gameHighestPossibleAmount = game.getHighestAvaiableAmount()
            if self.avaiable_amount <= gameHighestPossibleAmount:
                self.bet = self.bet + self.avaiable_amount
                print('You playied All in')
            else:
                print('You cannot play all in play raise to: ' + gameHighestPossibleAmount + ' instead')

    def setHand(self, hand):
        self.hand = hand


class Round:
    def __init__(self, players):
        self.players = players
        self.tableCards = []
        deck = Deck()
        deck.shuffle()
        for player in self.players:
            player.setHand = Hand(deck, 2)
        for i in range(5):
            self.tableCards[i] = deck.drawCard()

    def showThree(self):
        print(self.tableCards[0:2])
        return tableCards[1:3]

    def showFour(self):
        print(self.tableCards[0:3])
        return tableCards[1:4]

    def showFive(self):
        print(self.tableCards[0:4])
        return tableCards[1:5]


class pointCounter:

    def __init__(self):
        pass

    def compareSameResult(self, cardList1, cardList2, resultType):
        betterCombination = cardList1
        if resultType == 'Poker':
            if cardList1[0].figure >= cardList2[0].figure:
                if (cardList1[0].colour > cardList2[0].colour) or cardList1[0].figure > cardList2[0].figure:
                    betterCombination = cardList1
                else:
                    betterCombination = cardList2
            else:
                betterCombination = cardList2
        if resultType == 'Four of Kind':
            figure_list1 = [x.figure for x in cardList1]
            figure_list2 = [x.figure for x in cardList2]
            c1 = Counter(figure_list1)
            c2 = Counter(figure_list2)
            val1_fig, y1 = c1.most_common(2)[0]
            val2_fig, y2 = c1.most_common(2)[0]
            if val1_fig > val2_fig:
                betterCombination = cardList1
            else:
                betterCombination = cardList2
        if resultType == 'Full house':
            figure_list1 = [x.figure for x in cardList1]
            figure_list2 = [x.figure for x in cardList2]
            c1 = Counter(figure_list1)
            c2 = Counter(figure_list2)
            val1_fig, y1 = c1.most_common(2)[0]
            val2_fig, y2 = c1.most_common(2)[0]
            if val1_fig == val2_fig:
                val1_fig, y1 = c1.most_common(2)[1]
                val2_fig, y2 = c1.most_common(2)[1]
                if val1_fig > val2_fig:
                    betterCombination = cardList1
                else:
                    betterCombination = cardList2
            elif val1_fig > val2_fig:
                betterCombination = cardList1
            else:
                betterCombination = cardList2
        if resultType == 'Flush':
            if cardList1[0].colour > cardList2[0].colour:
                betterCombination = cardList1
            else:
                betterCombination = cardList2
        if resultType == 'Straight':
            if cardList1[0].figure > cardList2[0].figure:
                betterCombination = cardList1
            else:
                betterCombination = cardList2
        if resultType == 'Three of kind':
            figure_list1 = [x.figure for x in cardList1]
            figure_list2 = [x.figure for x in cardList2]
            c1 = Counter(figure_list1)
            c2 = Counter(figure_list2)
            val1_fig, y1 = c1.most_common(2)[0]
            val2_fig, y2 = c1.most_common(2)[0]
            if val1_fig == val2_fig:
                val1_fig, y1 = c1.most_common(2)[1]
                val2_fig, y2 = c1.most_common(2)[1]
                if val1_fig > val2_fig:
                    betterCombination = cardList1
                else:
                    betterCombination = cardList2
            elif val1_fig > val2_fig:
                betterCombination = cardList1
            else:
                betterCombination = cardList2
        if resultType == 'One pair':
            figure_list1 = [x.figure for x in cardList1]
            figure_list2 = [x.figure for x in cardList2]
            c1 = Counter(figure_list1)
            c2 = Counter(figure_list2)
            val1_fig, y1 = c1.most_common(2)[0]
            val2_fig, y2 = c1.most_common(2)[0]
            if val1_fig == val2_fig:
                val1_fig, y1 = c1.most_common(2)[1]
                val2_fig, y2 = c1.most_common(2)[1]
                if val1_fig > val2_fig:
                    betterCombination = cardList1
                else:
                    betterCombination = cardList2
            elif val1_fig > val2_fig:
                betterCombination = cardList1
            else:
                betterCombination = cardList2
        if resultType == 'High card':
            if cardList1[0].figure >= cardList2[0].figure:
                if (cardList1[0].colour > cardList2[0].colour) or cardList1[0].figure > cardList2[0].figure:
                    betterCombination = cardList1
                else:
                    betterCombination = cardList2
            else:
                betterCombination = cardList2

        return betterCombination

    def checkStraight(self, cardList):
        cardList.sort()
        for i in range(0, 4):
            if cardList[i].figure + 1 != cardList[i + 1].figure:
                return False
        return True

    def checkSameColour(self, cardList):
        colour_list = [x.colour for x in cardList]
        c = Counter(colour_list)
        x, y = c.most_common(1)[0]
        if y >= 4:
            return True
        return False

    def findSameFigures(self, cardList, quantity):
        figure_list = [x.figure for x in cardList]
        c = Counter(figure_list)
        x, y = c.most_common(1)[0]
        if y == quantity:
            return True
        return False

    def findFullHouse(self, cardList):
        figure_list = [x.figure for x in cardList]
        c = Counter(figure_list)
        x3, y3 = c.most_common(2)[0]
        x2, y2 = c.most_common(2)[1]
        if y3 == 3 and y2 == 2:
            return True
        return False

    def findTwoPair(self, cardList):
        figure_list = [x.figure for x in cardList]
        c = Counter(figure_list)
        x, y = c.most_common(2)[0]
        x2, y2 = c.most_common(2)[1]
        if y2 == 2 and y == 2:
            return True
        return False

    def generateCombinationFromTable(self, hand, tableCards):
        listOfResults = []
        for subset in itertools.combinations(tableCards, 3):
            card1, card2, card3 = subset
            possibleResult = []
            possibleResult.append(hand.cards[0])
            possibleResult.append(hand.cards[1])
            possibleResult.append(card1)
            possibleResult.append(card2)
            possibleResult.append(card3)
            listOfResults.append(possibleResult)

        return listOfResults

    def countBestResult(self, hand, tableCards):

        def assignBest(combination, bestCombination, resultType, best):
            if best == GetResultName(resultType):
                bestCombination = self.compareSameResult(combination, bestCombination, resultType)
            else:
                bestCombination = combination
            best = GetResultName(resultType)
            return best, bestCombination

        listOfCombinations = self.generateCombinationFromTable(hand = hand, tableCards = tableCards)
        best = -1
        bestCombination = []
        for combination in listOfCombinations:
            combination.sort()
            if self.checkStraight(combination) and self.checkSameColour(combination) and best <= GetResultName('Poker'):
                best, bestCombination = assignBest(combination, bestCombination, 'Poker', best)
            if self.findSameFigures(combination, 4) and best <= GetResultName('Four of Kind'):
                best, bestCombination = assignBest(combination, bestCombination, 'Four of Kind', best)
            if self.findFullHouse(combination) and best <= GetResultName('Full house'):
                best, bestCombination = assignBest(combination, bestCombination, 'Full house', best)
            if self.checkSameColour(combination) and best <= GetResultName('Flush'):
                best, bestCombination = assignBest(combination, bestCombination, 'Flush', best)
            if self.checkStraight(combination) and best <= GetResultName('Straight'):
                best, bestCombination = assignBest(combination, bestCombination, 'Straight', best)
            if self.findSameFigures(combination, 3) and best <= GetResultName('Three of kind'):
                best, bestCombination = assignBest(combination, bestCombination, 'Three of kind', best)
            if self.findTwoPair(combination) and best <= GetResultName('Two pair'):
                best, bestCombination = assignBest(combination, bestCombination, 'Two pair', best)
            if self.findSameFigures(combination, 2) and best <= GetResultName('One pair'):
                best, bestCombination = assignBest(combination, bestCombination, 'One pair', best)
            if best <= GetResultName('High card'):
                best, bestCombination = assignBest(combination, bestCombination, 'High card', best)

        return best, bestCombination


class Table():
    def __init__(self):
        self.sits = []

    def take_sit(self, player):
        if len(self.sits) == 4:
            raise Exception("Table is full")
        self.sits.append(player)

    def display(self):
        names =[]
        for i in range(4):
            if self.sits[i]:
                names.append(self.sits[i].name)
            names.append("X")
        return (names)

    def startRound(self):
        r = Round(self.sits)
        return r


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck, 2)
    tableCards = []
    tableCards.append(deck.drawCard())
    tableCards.append(deck.drawCard())
    tableCards.append(deck.drawCard())
    tableCards.append(deck.drawCard())
    tableCards.append(deck.drawCard())

    pointCounter = pointCounter()
    best, bestCombination = pointCounter.countBestResult(hand = hand, tableCards = tableCards)
    print(best)
    for i in bestCombination:
        print(i)

    p1 = Player("A")
    p2 = Player("B")

    t = Table()
    t.take_sit(p1)
    t.take_sit(p2)

    r = t.startRound()

    r.showThree()


    print('Choose play :\n 1 - fold \n 2 - check  \n 3 - call \n 4 - raise \n 5 - all in')
    # print(hand)
