import random

from src import run

logger = run.get_loggerObject()

suits = ['Spades','Diamonds','Clubs','Hearts']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Players():
    def __init__(self,assumption_win = 0,jokers_on_hand = 0):
        self.hand = []
        self.assumption_win = assumption_win
        self.jokers_on_hand = jokers_on_hand
        self.turn = False

    def add_to_hand(self,deal):
        logger.info(f"Adding into hand : {deal}")
        self.hand.append(deal)

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank,values[rank]))
        random.shuffle(self.deck)

class Card():
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = {}

class Round():
    def __init__(self,players=[],deck=[],round_joker =''):
        self.players = players
        self.deck = deck
        self.round_joker = round_joker # This comes from the Players turn.

    def get_round_joker(self,game_number):
        random.shuffle(self.deck)
        logger.info(f"# Getting Round Joker for Round {game_number}")
        return self.deck.pop()

    def deal(self):
        single_card = self.deck.pop()
        logger.info(f"Dealing a card from the deck : {single_card}")
        return single_card

class Game():
    game_number = 10
    round_number = 10
    def __init__(self,main_joker = 'Spades'):
        self.round_wins = []
        self.main_joker = main_joker

    def get_main_joker(self): # This is given by Dealer
        tSuits = ['Spades','Diamonds','Clubs','Hearts']
        random.shuffle(tSuits)
        popped = tSuits.pop()
        logger.info(f"# Getting the Main Joker : {popped}")
        return popped

    def create_players(self,number_of_players):
        logger.info(f"# Initializing Empty Players to the table")
        players = []
        for i in range(0,number_of_players):
            players.append(Players())
        return players

    def sub_round(self,sub_rounds):
        # This is where the game is played. number of player's turns
        pass
    def main_round(self,main_rounds):
        # A Main_round contains 10 sub-rounds
        while main_rounds:
            pass
    def single_game(self):
        # Single_game contains 10 main rounds
        playerNum = 1
        players = self.create_players(playerNum)
        deck = Deck()
        logger.info(f"# Initializing the game Judgement")

    # def insideRoundDecision(self):
    #     #playerCount = int(input("How many Players?"))
    #     playerCount = 3
    #     players = self.create_players(playerCount)
    #     deck = Deck()
    #     while self.game_number:
    #         logger.info(f"Entering the Game : {self.game_number}")
    #         self.get_main_joker()
    #         while playerCount :
    #             self.round_number = 10
    #             while self.round_number:
    #                 logger.info(f"Initializing Round {self.round_number} of Game {self.game_number} ")
    #                 R = Round(players,deck)
    #                 print(R)
    #                 self.round_number -= 1
    #     print(f"Reaching : {self.game_number}")
    #     self.game_number -= 1

"""
A Single game consists of 10 rounds and 10 sub-rounds
"""


"""
A Game consists of game_number of rounds.
so there are in total 10 * 10 rounds
"""

G1 = Game()
G1.single_game()


