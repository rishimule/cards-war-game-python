#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__ = "0.2.0"
__author__  = "Radon Gas"
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2020 Radon Gas (radonintro1234)'

"""
Author  : Radon Gas (radonintro1234)
Github  : https://github.com/radonintro1234
License : MIT
Copyright (c) 2020 Radon Gas (radonintro1234)
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

from random import shuffle

suits = ["Hearts", "Spades" ,"Clubs", "Diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" , "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two"   : 2,
          "Three" : 3,
          "Four"  : 4,
          "Five"  : 5,
          "Six"   : 6,
          "Seven" : 7,
          "Eight" : 8,
          "Nine"  : 9,
          "Ten"   : 10,
          "Jack"  : 11,
          "Queen" : 12,
          "King"  : 13,
          "Ace"   : 14
          }

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class Card():
    """Class to create a card"""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        "Function to print the Card"
        return str(self.rank) + " of " + self.suit + "."

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class Deck():
    """Class to create a Deck"""

    def __init__(self):
        self.deck_list = []

        for rank in ranks:
            for suit in suits:
                temp_card = Card(rank,suit)
                self.deck_list.append(temp_card)

        shuffle(self.deck_list)

    def __str__(self):
        "Function to print a deck"
        return str("This deck has ") + str(len(self.deck_list)) + str(" cards.")

    def popCard(self):
        "Function to pop the Top Card"
        return self.deck_list.pop()

    def shuffleDeck(self):
        "Function to manually shuffle the Deck"
        shuffle(self.deck_list)

    def viewCards(self):
        "Function to viewall the cards of a Deck"
        for card in self.deck_list:
            print(card)

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class Player():
    """Class to create a Player"""

    def __init__(self, name):
        self.name = name
        self.player_deck = []

    def __str__(self):
        "Function to print Player Properties"
        return self.name + " has " + str(len(self.player_deck)) + " Cards."

    def addCard(self, card):
        "Function to add a card to Player's Deck"
        self.player_deck.append(card)
        shuffle(self.player_deck)

    def popCard(self):
        "Function to pop a card from Player's Deck"
        shuffle(self.player_deck)
        return self.player_deck.pop()

    def viewCards(self):
        "Function to view all the player's Current cards"
        for card in self.player_deck:
            print(card)

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def main():
    # Start the program
    current_players = []
    deck1 = Deck()
    print(deck1)

    temp_name = str(input("Give a Player1 name : "))
    player1 = Player(temp_name)
    current_players.append(player1)

    temp_name = str(input("Give a Player2 name : "))
    player2 = Player(temp_name)
    current_players.append(player2)

    temp_name = str(input("Give a Player3 name : "))
    player3 = Player(temp_name)
    current_players.append(player3)

    while len(deck1.deck_list) != 0:
        if len(deck1.deck_list) == 0:
            break
        player1.addCard(deck1.popCard())

        if len(deck1.deck_list) == 0:
            break
        player2.addCard(deck1.popCard())

        if len(deck1.deck_list) == 0:
            break
        player3.addCard(deck1.popCard())

    print(player1)
    print(player2)
    print(player3)

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    round_no = 0

    while(len(current_players) == 3):
        round_no += 1
        print("-" *100)
        print("Round " + str(round_no) + " :-")

        player1_popdeck = []
        player2_popdeck = []
        player3_popdeck = []

        player1_popdeck.append(player1.popCard())
        player2_popdeck.append(player2.popCard())
        player3_popdeck.append(player3.popCard())

        a=player1_popdeck[-1].value
        b=player2_popdeck[-1].value
        c=player3_popdeck[-1].value

        print("Comparison : " + str(player1_popdeck[-1]) + " -vs- " + str(player2_popdeck[-1]) + " -vs- " + str(player3_popdeck[-1]))

        if (a>b and a>c):
            print("Round Winner: " + player1.name)
            player1.player_deck.extend(player1_popdeck)
            player1.player_deck.extend(player2_popdeck)
            player1.player_deck.extend(player3_popdeck)

        if (b>a and b>c):
            print("Round Winner: " + player2.name)
            player2.player_deck.extend(player1_popdeck)
            player2.player_deck.extend(player2_popdeck)
            player2.player_deck.extend(player3_popdeck)

        if (c>a and c>b):
            print("Round Winner: " + player3.name)
            player3.player_deck.extend(player1_popdeck)
            player3.player_deck.extend(player2_popdeck)
            player3.player_deck.extend(player3_popdeck)

        # -------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------

        if (a==b and a>c):
            while(a==b):
                print("a=b war..... lets try again!\n")

                if len(player1.player_deck) == 0:
                    print(player1.name + " Has an Empty Deck\n")
                    current_players.remove(player1)

                    print("Round Winner: " + player2.name)
                    player2.player_deck.extend(player1_popdeck)
                    player2.player_deck.extend(player2_popdeck)
                    player2.player_deck.extend(player3_popdeck)
                    break

                if len(player2.player_deck) == 0:
                    print(player2.name + " Has an Empty Deck\n")
                    current_players.remove(player2)

                    print("Round Winner: " + player1.name)
                    player1.player_deck.extend(player1_popdeck)
                    player1.player_deck.extend(player2_popdeck)
                    player1.player_deck.extend(player3_popdeck)
                    break

                player1_popdeck.append(player1.popCard())
                player2_popdeck.append(player2.popCard())
                a=player1_popdeck[-1].value
                b=player2_popdeck[-1].value
                print("Comparison : " + str(player1_popdeck[-1]) + " -vs- " + str(player2_popdeck[-1]))

                if(a>b):
                    print("Round Winner: " + player1.name)
                    player1.player_deck.extend(player1_popdeck)
                    player1.player_deck.extend(player2_popdeck)
                    player1.player_deck.extend(player3_popdeck)

                if(b>a):
                    print("Round Winner: " + player2.name)
                    player2.player_deck.extend(player1_popdeck)
                    player2.player_deck.extend(player2_popdeck)
                    player2.player_deck.extend(player3_popdeck)
        # -------------------------------------------------------------------------------------------------

        if (b==c and b>a):
            while(b==c):
                print("b=c war..... lets try again!\n")

                if len(player2.player_deck) == 0:
                    print(player2.name + " Has an Empty Deck\n")
                    current_players.remove(player2)

                    print("Round Winner: " + player3.name)
                    player3.player_deck.extend(player1_popdeck)
                    player3.player_deck.extend(player2_popdeck)
                    player3.player_deck.extend(player3_popdeck)
                    break

                if len(player3.player_deck) == 0:
                    print(player3.name + " Has an Empty Deck\n")
                    current_players.remove(player3)

                    print("Round Winner: " + player2.name)
                    player2.player_deck.extend(player1_popdeck)
                    player2.player_deck.extend(player2_popdeck)
                    player2.player_deck.extend(player3_popdeck)
                    break

                player2_popdeck.append(player2.popCard())
                player3_popdeck.append(player3.popCard())

                b=player2_popdeck[-1].value
                c=player3_popdeck[-1].value
                print("Comparison : " + str(player2_popdeck[-1]) + " -vs- " + str(player3_popdeck[-1]))

                if(b>c):
                    print("Round Winner: " + player2.name)
                    player2.player_deck.extend(player1_popdeck)
                    player2.player_deck.extend(player2_popdeck)
                    player2.player_deck.extend(player3_popdeck)

                if(c>b):
                    print("Round Winner: " + player3.name)
                    player3.player_deck.extend(player1_popdeck)
                    player3.player_deck.extend(player2_popdeck)
                    player3.player_deck.extend(player3_popdeck)

        # -------------------------------------------------------------------------------------------------

        if (a==c and a>b):
            while(a==c):
                print("a=c war..... lets try again!\n")

                if len(player1.player_deck) == 0:
                    print(player1.name + " Has an Empty Deck\n")
                    current_players.remove(player1)

                    print("Round Winner: " + player3.name)
                    player3.player_deck.extend(player1_popdeck)
                    player3.player_deck.extend(player2_popdeck)
                    player3.player_deck.extend(player3_popdeck)
                    break

                if len(player3.player_deck) == 0:
                    print(player3.name + " Has an Empty Deck\n")
                    current_players.remove(player3)

                    print("Round Winner: " + player1.name)
                    player1.player_deck.extend(player1_popdeck)
                    player1.player_deck.extend(player2_popdeck)
                    player1.player_deck.extend(player3_popdeck)
                    break

                player1_popdeck.append(player1.popCard())
                player3_popdeck.append(player3.popCard())

                a=player1_popdeck[-1].value
                c=player3_popdeck[-1].value
                print("Comparison : " + str(player1_popdeck[-1])  + " -vs- " + str(player3_popdeck[-1]))

                if(a>c):
                    print("Round Winner: " + player1.name)
                    player1.player_deck.extend(player1_popdeck)
                    player1.player_deck.extend(player2_popdeck)
                    player1.player_deck.extend(player3_popdeck)

                if(c>a):
                    print("Round Winner: " + player3.name)
                    player3.player_deck.extend(player1_popdeck)
                    player3.player_deck.extend(player2_popdeck)
                    player3.player_deck.extend(player3_popdeck)

        # -------------------------------------------------------------------------------------------------
        # check if any player has zero cards left
        try:
            if len(player1.player_deck) == 0:
                print(player1.name + " Has an Empty Deck\n")
                current_players.remove(player1)
        except:
            pass

        try:
            if len(player2.player_deck) == 0:
                print(player2.name + " Has an Empty Deck\n")
                current_players.remove(player2)
        except:
            pass

        try:
            if len(player3.player_deck) == 0:
                print(player3.name + " Has an Empty Deck\n")
                current_players.remove(player3)
        except:
            pass

    # -----------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------

    if len(current_players) == 1:
        print("-" *100)
        print(current_players[0].name + " wins!")

    elif len(current_players) == 2:
        print("-" *100)
        print("Only Two Players Remaning : " + current_players[0].name + " and " + current_players[1].name)
        game_on = True
        player_one = current_players[0]
        player_two = current_players[1]

        while game_on:
            print("-" *100)
            round_no += 1
            print(f"Round {round_no}")

            if len(player_one.player_deck)==0:
                print("-"*100)
                print(player_one.name + " has an Empty Deck.\n")
                print("-"*100)
                print("-"*100)
                print( player_two.name + " wins.\n")
                print("-"*100)
                print("-"*100)
                game_on = False
                break

            if len(player_two.player_deck)==0:
                print("-"*100)
                print(player_two.name + " has an empty Deck.\n")
                print("-"*100)
                print("-"*100)
                print(player_one.name + " wins.\n")
                print("-"*100)
                print("-"*100)
                game_on = False
                break

            player_one_cards = []
            player_one_cards.append(player_one.popCard())

            player_two_cards = []
            player_two_cards.append(player_two.popCard())

            is_war = True

            while is_war:

                print("Comparison : " + str(player_one_cards[-1]) + " -vs- " + str(player_two_cards[-1]))

                if player_one_cards[-1].value > player_two_cards[-1].value :

                    player_one.player_deck.extend(player_one_cards)
                    player_one.player_deck.extend(player_two_cards)
                    print("Round Winner : " + player_one.name)

                    is_war = False
                    break

                elif player_one_cards[-1].value < player_two_cards[-1].value :

                    player_two.player_deck.extend(player_one_cards)
                    player_two.player_deck.extend(player_two_cards)
                    print("Round Winner : " + player_two.name)

                    is_war = False
                    break

                else:
                    print('WAR! WAR! WAR! WAR! WAR!\n')
                    # This occurs when the cards are equal.
                    # We'll grab another card each and continue the current war.

                    # First check to see if player has enough cards

                    # Check to see if a player is out of cards:

                    if len(player_one.player_deck) == 0:
                        print("-"*100)
                        print(player_one.name + " has an Empty Deck.\n")
                        print("-"*100)
                        print("-"*100)
                        print( player_two.name + " Wins!\n")
                        print("-"*100)
                        print("-"*100)
                        game_on = False
                        break

                    elif len(player_two.player_deck) == 0:
                        print("-"*100)
                        print(player_two.name + " has an Empty Deck.\n")
                        print("-"*100)
                        print("-"*100)
                        print( player_one.name + " Wins!\n")
                        print("-"*100)
                        print("-"*100)
                        game_on = False
                        break
                    # Otherwise, we're still at war, so we'll add the next cards
                    else:
                        player_one_cards.append(player_one.popCard())
                        player_two_cards.append(player_two.popCard())

    else:
        print("ERROR!!!!!!!\n")

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
if __name__ == '__main__':
    main()
