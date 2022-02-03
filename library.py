import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}



dealer_cards = []
dealer_sum = 0
player_cards = []
player_sum = 0

#class card
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"



#class deck
class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank)
                self.deck.append(new_card)
    def number(self):
        return len(self.deck)
    def hit(self):
        return self.deck.pop()
    def suffle(self):
        random.shuffle(self.deck)

#class bank_roll
class Bank():
    def __init__(self,amount):
        self.amount = amount
    def win(self,value):
        self.amount+=value*2
    def lose(self,value):
        self.amount-=value

