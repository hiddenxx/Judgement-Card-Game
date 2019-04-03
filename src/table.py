import random
suits = ('Spades' , 'Diamonds' , 'Clubs' , 'Hearts')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Players():
    def __init__(self,assumption_win,jokers_on_hand = 0,round_wins = 0):
        self.hand = []
        self.assumption_win = assumption_win
        self.jokers_on_hand = jokers_on_hand

    def add_to_hand(self,deal):
        self.hand.append(deal)

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank,values[rank]))
        self.shuffle()

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
class Round():
    def __init__(self,players,deck,round_joker):
        self.players = players
        self.deck = deck
        self.round_joker = round_joker # This comes from the Players turn.

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Game():
    game_number = 10
    def __init__(self,main_joker):
        self.round_wins = []
        self.main_joker = main_joker

    def get_main_joker(self):
        tSuits = random.shuffle(suits)
        return tSuits.pop()

    def turnDecision(self):
        pass


