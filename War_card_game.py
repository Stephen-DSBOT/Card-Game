#define some global variables

suits= ['Hearts','Diamonds','Spades','Clubs']
ranks= ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values={'Two':2, 'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}


	#CARD CLASS

class Card():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


     #CARD CLASS

#importing the random library
import random


class Deck():
    
    def __init__(self):
        self.all_cards= []
        
        

	for suit in suits:
		for rank in ranks:

			#creating the chosen card 
			chosen_card = Card(suit,rank)
			self.all_cards.append(chosen_card)

    def shuffle(self):
    	random.shuffle(selfall_cards)

    def deal_one(self):
    	return self.all_cards.pop()




        # Player Class

class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards= []
        
    def remove_card(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards '




        # Game Setup

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())




# While loops

game_on= True
counter = 0

while game_on:
    
    #Game Counter
    counter +=1
    print(f'Round {counter}')
    
    #Game check
    #check if player_one lose
    if len(player_one.all_cards) == 0:
        print(f'player_one out of cards, player_two wins')
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print(f'player_two out of cards, player_one wins')
        game_on = False
        break
        
        
    # Start a new game
    player_one_cards = []
    player_two_cards = []
    
    player_one_cards.append(player_one.remove_card())
    player_two_cards.append(player_two.remove_card())
    
    
    at_war = True
    
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        else:
            print('War!!')
            if len(player_one.all_cards) < 5:
                print("player_one don't have enough cards \nplayer_two wins")
                game_on = False
                break
                
            elif len(player_two.all_cards) < 5: 
                print("player_two don't have enough cards \nplayer_one wins")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
                    
