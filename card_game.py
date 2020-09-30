# CARD WAR GAME...... 
# by RadonGas

from random import shuffle

suits = ("Hearts", "Clubs", "Diamonds", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" :7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 11, "Queen" : 12, "King" : 13, "Ace" : 14}

class Card:
    
    """
    This Class creates a Card of a particular Suit and Rank.
    """
    
    def __init__(self,rank,suit):
        
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        """
        Printing a Card
        """
        return self.rank + " of " + self.suit
        
class Deck:
    """
    This Class creates a DECK, to be used while playing a game.
    """
    
    def __init__(self):
        
        self.cardlist = []
        
        
        #CREATING A DECK {LIST} OF CARDS FOR A GAME.
        
        for suit in suits:
            for rank in ranks:
                
                current_card = Card(rank,suit)
                
                self.cardlist.append(current_card)
                
        
    def __str__(self):
        """
        PRINTING A DECK.
        """
        return 'This Deck has {} Cards.'.format(str(len(self.cardlist)))
    
    def shuffle_deck(self):
        """
        Function For Shuffling a DECK.
        """
        shuffle(self.cardlist)
        shuffle(self.cardlist)
        
    def deal_one(self):
        """
        Function for Dealing a Card.
        """
        return self.cardlist.pop(0)
    
class Player():
    """
    This Class creates a player for playing the Game of War.
    """
    
    def __init__(self, name):
        
        self.name = name
        
        self.player_cards = []
        
    def __str__(self):
    	"""
    	Print Number of Cards of a Player.
    	"""
    	return f"Player {self.name} has {len(self.player_cards)} cards."
    
    def remove_card(self):
        """
        This function is used to POP a card from the top of the player deck.
        """
        
        return self.player_cards.pop(0)
    
    def add_cards(self,card_add):
        """
        This Function is used to add the cards to the player's deck who Wins!
        """
        
        if type(card_add) == type([]):
            self.player_cards.extend(card_add)
        else:
            self.player_cards.append(card_add)

def play_game():
	"""
	Start The Game
	"""
        
	#START A NEW DECK......

	new_deck = Deck()
	new_deck.shuffle_deck()

	#INITIATE PLAYERS

	player_one = Player("Radon")

	player_two = Player("Neon")

	#DISTRIBUTE THE DECK

	for x in range(0,26):
	    player_one.add_cards(new_deck.deal_one())
	    player_two.add_cards(new_deck.deal_one())

	print(player_one)
	print(player_two)

	#START LOGIC

	game_on = True

	round_no = 0

	while game_on:
	    
	    round_no += 1
	    print(f"Round {round_no}")
	    
	    if len(player_one.player_cards)==0:
	        print("\nPlayer Radon out of Cards.")
	        print("Player NEON wins.\n")
	        game_on = False
	        break
	        
	    if len(player_two.player_cards)==0:
	        print("\nPlayer Neon out of Cards.")
	        print("Player RADON wins.\n")
	        game_on = False
	        break
	        
	        
	    player_one_cards = []
	    player_one_cards.append(player_one.remove_card())
	    
	    player_two_cards = []
	    player_two_cards.append(player_two.remove_card())

	    is_war = True
	    
	    
	        
	    while is_war:
	            
	        if player_one_cards[-1].value > player_two_cards[-1].value :
	            
	            player_one.add_cards(player_one_cards)
	            player_one.add_cards(player_two_cards)
	            print("Added Card to Player 1 - Radon\n")
	            
	            is_war = False
	            break
	            
	                
	            
	        elif player_one_cards[-1].value < player_two_cards[-1].value :
	            
	            player_two.add_cards(player_one_cards)
	            player_two.add_cards(player_two_cards)
	            print("Added Card to Player 2 - Neon\n")
	            
	            is_war = False
	            break
	            
	            
	        else:
	            print('WAR! WAR! WAR! WAR! WAR!')
	            # This occurs when the cards are equal.
	            # We'll grab another card each and continue the current war.
	            
	            # First check to see if player has enough cards
	            
	            # Check to see if a player is out of cards:
	            
	            if len(player_one.player_cards) < 5:
	                print("Player One unable to play war! Game Over at War")
	                print("Player Two Wins!")
	                game_on = False
	                break

	            elif len(player_two.player_cards) < 5:
	                print("Player Two unable to play war! Game Over at War")
	                print("Player One Wins!")
	                game_on = False
	                break
	            # Otherwise, we're still at war, so we'll add the next cards
	            else:
	                for num in range(5):
	                    player_one_cards.append(player_one.remove_card())
	                    player_two_cards.append(player_two.remove_card())
	            

if __name__ == '__main__':
	
	play_game()

# by RadonGas