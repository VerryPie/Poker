import unittest
import Poker
from unittest.mock import patch

class testDeck(unittest.TestCase):
    def test_deck_size(self):
        self.assertEqual(len(Poker.Deck().cardList),52)
    def test_draw_card(self):
        deck = Poker.Deck()
        deck.drawCard()
        self.assertEqual(len(deck.cardList),51)

class testHand(unittest.TestCase):
    def test_hand_size(self):
        deck = Poker.Deck()
        hand = Poker.Hand(deck, 2)
        self.assertEqual(len(hand.cards),2)

    def test_deck_size(self):
        deck = Poker.Deck()
        hand = Poker.Hand(deck, 2)
        self.assertEqual(len(deck.cardList),50)

class testCard(unittest.TestCase):
    def test_get_figure_name(self):
        card = Poker.Card(0,11)
        self.assertEqual( 'JACK', card.getFigureName())

    def test_get_colour_name(self):
        card = Poker.Card(2, 11)
        self.assertEqual('DIMONDS', card.geColourName(),)

    def test_card_printer(self):
        card = Poker.Card(1, 12)
        self.assertEqual('Card colour is HEARTS and figure is QUEEN',str(card))

    def test_card_printer2(self):
        card = Poker.Card(0, 3)
        self.assertEqual('Card colour is SPADES and figure is 3',str(card))

class testResultCounting(unittest.TestCase):

    def test_checkStraightTrue(self):
        card1 = Poker.Card( figure=2, colour=0)
        card2 = Poker.Card( figure=4, colour=4)
        card3 = Poker.Card( figure=5, colour=0)
        card4 = Poker.Card( figure=6, colour=1)
        card5 = Poker.Card( figure=3, colour=0)
        cardList = [card1,card2,card3,card4,card5]
        pointCounter = Poker.pointCounter()
        self.assertTrue(pointCounter.checkStraight(cardList))

    def test_checkStraightFalse(self):
        card1 = Poker.Card( figure=10, colour=0)
        card2 = Poker.Card( figure=11, colour=4)
        card3 = Poker.Card( figure=12, colour=0)
        card4 = Poker.Card( figure=5, colour=1)
        card5 = Poker.Card( figure=5, colour=0)
        cardList = [card1,card2,card3,card4,card5]
        pointCounter = Poker.pointCounter()
        self.assertFalse(pointCounter.checkStraight(cardList))


    def test_checkSameColour(self):
        card1 = Poker.Card( figure=10, colour=0)
        card2 = Poker.Card( figure=5, colour=0)
        card3 = Poker.Card( figure=12, colour=0)
        card4 = Poker.Card( figure=5, colour=0)
        card5 = Poker.Card( figure=5, colour=0)
        cardList = [card1,card2,card3,card4,card5]
        pointCounter = Poker.pointCounter()
        self.assertTrue(pointCounter.checkSameColour(cardList))

    def test_checkSameColourFalse(self):
        card1 = Poker.Card(figure=10, colour=0)
        card2 = Poker.Card(figure=5, colour=1)
        card3 = Poker.Card(figure=12, colour=3)
        card4 = Poker.Card(figure=5, colour=0)
        card5 = Poker.Card(figure=5, colour=1)
        cardList = [card1, card2, card3, card4, card5]
        pointCounter = Poker.pointCounter()
        self.assertFalse(pointCounter.checkSameColour(cardList))

    def test_findSameFigures(self):
        card1 = Poker.Card(figure=10, colour=0)
        card2 = Poker.Card(figure=5, colour=1)
        card3 = Poker.Card(figure=12, colour=3)
        card4 = Poker.Card(figure=5, colour=0)
        card5 = Poker.Card(figure=5, colour=1)
        cardList = [card1, card2, card3, card4, card5]
        pointCounter = Poker.pointCounter()
        self.assertTrue(pointCounter.findSameFigures(cardList,3))

    def test_findSameFiguresFalse(self):
        card1 = Poker.Card(figure=10, colour=0)
        card2 = Poker.Card(figure=5, colour=1)
        card3 = Poker.Card(figure=12, colour=3)
        card4 = Poker.Card(figure=2, colour=0)
        card5 = Poker.Card(figure=1, colour=1)
        cardList = [card1, card2, card3, card4, card5]
        pointCounter = Poker.pointCounter()
        self.assertFalse(pointCounter.findSameFigures(cardList,3))

    def test_findFullHouse(self):
        card1 = Poker.Card(figure=10, colour=0)
        card2 = Poker.Card(figure=5, colour=1)
        card3 = Poker.Card(figure=5, colour=3)
        card4 = Poker.Card(figure=10, colour=0)
        card5 = Poker.Card(figure=5, colour=1)
        cardList = [card1, card2, card3, card4, card5]
        pointCounter = Poker.pointCounter()
        self.assertTrue(pointCounter.findFullHouse(cardList))

    def test_findFullHouseFalse(self):
        card1 = Poker.Card(figure=10, colour=0)
        card2 = Poker.Card(figure=5, colour=1)
        card3 = Poker.Card(figure=2, colour=3)
        card4 = Poker.Card(figure=10, colour=0)
        card5 = Poker.Card(figure=5, colour=1)
        cardList = [card1, card2, card3, card4, card5]
        pointCounter = Poker.pointCounter()
        self.assertFalse(pointCounter.findFullHouse(cardList))

    def test_findTwoPair(self):
        card1 = Poker.Card(figure=10, colour=0)
        card2 = Poker.Card(figure=5, colour=1)
        card3 = Poker.Card(figure=5, colour=3)
        card4 = Poker.Card(figure=10, colour=0)
        card5 = Poker.Card(figure=3, colour=1)
        cardList = [card1, card2, card3, card4, card5]
        pointCounter = Poker.pointCounter()
        self.assertTrue(pointCounter.findTwoPair(cardList))

    def test_findTwoPairFalse(self):
        card1 = Poker.Card(figure=10, colour=0)
        card2 = Poker.Card(figure=5, colour=1)
        card3 = Poker.Card(figure=3, colour=3)
        card4 = Poker.Card(figure=10, colour=0)
        card5 = Poker.Card(figure=13, colour=1)
        cardList = [card1, card2, card3, card4, card5]
        pointCounter = Poker.pointCounter()
        self.assertFalse(pointCounter.findTwoPair(cardList))

    @patch("Poker.Hand")
    def test_generateCombinationFromTableLength(self):
        card1 = Poker.Card(figure=2, colour=0)
        card2 = Poker.Card(figure=3, colour=1)
        card3 = Poker.Card(figure=4, colour=3)
        card4 = Poker.Card(figure=5, colour=3)
        card5 = Poker.Card(figure=6, colour=1)
        card6 = Poker.Card(figure=7, colour=2)
        card7 = Poker.Card(figure=12, colour=1)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5, card6, card7]
        pointCounter = Poker.pointCounter()
        self.assertEqual(10,len(pointCounter.generateCombinationFromTable(cardList1, cardList2)))


    def test_PokerCombination(self):
        card1 = Poker.Card(figure=4, colour=0)
        card2 = Poker.Card(figure=5, colour=0)
        card3 = Poker.Card(figure=8, colour=0)
        card4 = Poker.Card(figure=6, colour=0)
        card5 = Poker.Card(figure=7, colour=0)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5]
        pointCounter = Poker.pointCounter()
        best ,bestResultList = pointCounter.countBestResult(cardList1, cardList2)
        self.assertEqual(best, Poker.GetResultName('Poker'))

    def test_FourOfKindCombination(self):
        card1 = Poker.Card(figure=7, colour=0)
        card2 = Poker.Card(figure=7, colour=1)
        card3 = Poker.Card(figure=7, colour=2)
        card4 = Poker.Card(figure=6, colour=3)
        card5 = Poker.Card(figure=7, colour=3)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5]
        pointCounter = Poker.pointCounter()
        best ,bestResultList = pointCounter.countBestResult(cardList1, cardList2)
        self.assertEqual(best, Poker.GetResultName('Four of Kind'))

    def test_FullHouseCombination(self):
        card1 = Poker.Card(figure=7, colour=0)
        card2 = Poker.Card(figure=12, colour=1)
        card3 = Poker.Card(figure=12, colour=2)
        card4 = Poker.Card(figure=7, colour=1)
        card5 = Poker.Card(figure=7, colour=3)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5]
        pointCounter = Poker.pointCounter()
        best ,bestResultList = pointCounter.countBestResult(cardList1, cardList2)
        self.assertEqual(best, Poker.GetResultName('Full house'))

    def test_FlushCombination(self):
        card1 = Poker.Card(figure=7, colour=0)
        card2 = Poker.Card(figure=10, colour=1)
        card3 = Poker.Card(figure=12, colour=1)
        card4 = Poker.Card(figure=5, colour=1)
        card5 = Poker.Card(figure=13, colour=1)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5]
        pointCounter = Poker.pointCounter()
        best ,bestResultList = pointCounter.countBestResult(cardList1, cardList2)
        self.assertEqual(best, Poker.GetResultName('Flush'))

    def test_StraightCombination(self):
        card1 = Poker.Card(figure=11, colour=0)
        card2 = Poker.Card(figure=10, colour=1)
        card3 = Poker.Card(figure=12, colour=3)
        card4 = Poker.Card(figure=9, colour=2)
        card5 = Poker.Card(figure=13, colour=1)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5]
        pointCounter = Poker.pointCounter()
        best ,bestResultList = pointCounter.countBestResult(cardList1, cardList2)
        self.assertEqual(best, Poker.GetResultName('Straight'))

    def test_ThreeOfKindCombination(self):
        card1 = Poker.Card(figure=9, colour=0)
        card2 = Poker.Card(figure=9, colour=1)
        card3 = Poker.Card(figure=12, colour=3)
        card4 = Poker.Card(figure=9, colour=2)
        card5 = Poker.Card(figure=13, colour=1)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5]

        pointCounter = Poker.pointCounter()
        best ,bestResultList = pointCounter.countBestResult(cardList1, cardList2)
        self.assertEqual(best, Poker.GetResultName('Three of kind'))

    def test_TwoPairCombination(self):
        card1 = Poker.Card(figure=9, colour=0)
        card2 = Poker.Card(figure=2, colour=1)
        card3 = Poker.Card(figure=13, colour=3)
        card4 = Poker.Card(figure=9, colour=2)
        card5 = Poker.Card(figure=13, colour=1)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5]
        pointCounter = Poker.pointCounter()
        best ,bestResultList = pointCounter.countBestResult(cardList1, cardList2)
        self.assertEqual(best, Poker.GetResultName('Two pair'))

    def test_OnePairCombination(self):
        card1 = Poker.Card(figure=14, colour=0)
        card2 = Poker.Card(figure=2, colour=1)
        card3 = Poker.Card(figure=13, colour=3)
        card4 = Poker.Card(figure=9, colour=2)
        card5 = Poker.Card(figure=13, colour=1)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5]
        pointCounter = Poker.pointCounter()
        best ,bestResultList = pointCounter.countBestResult(cardList1, cardList2)
        self.assertEqual(best, Poker.GetResultName('One pair'))

    def test_HighCardCombination(self):
        card1 = Poker.Card(figure=14, colour=0)
        card2 = Poker.Card(figure=2, colour=1)
        card3 = Poker.Card(figure=11, colour=3)
        card4 = Poker.Card(figure=9, colour=2)
        card5 = Poker.Card(figure=13, colour=1)
        cardList1 = [card1, card2]
        cardList2 = [card3, card4, card5]
        pointCounter = Poker.pointCounter()
        best ,bestResultList = pointCounter.countBestResult(cardList1, cardList2)
        self.assertEqual(best, Poker.GetResultName('High card'))

if __name__ == '__main__':
    unittest.main()
