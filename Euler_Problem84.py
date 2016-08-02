# Monopoly Odds
# Problem Source: https://projecteuler.net/problem=84
# Approach: 1. We are going to solve the problem by using simulation. i.e we will simulate throwing a pair of dice and moving the tokens around the board a million times. 

# Data Structures needed:
# An iterable  to maintain the "Chance" cards.
# An iterable to store "Community Chest " cards.
# An iterable (of length n for n simulations) to keep track of which square the player landed on, finally, at the end of every simulation. 



# Things to do:
# Simulate the roll of 2 6-sided dice.

# For the Community Chest card: 
# a) There are 16 CC cards. Shuffle the cards at the start of the game. This is achieved by randomly sampling without replacement 16 numbers in the range (1,16) both inclusive.
# b) According to the problem rules, only card numbers 1 and 2 order a movement. If we draw any other number, we dont move anywhere i.e. we do nothing.
# c) Each time the player lands on the Community Chest square, get the first number (and the corresponding chance card) from the beginning of the random list. 
# d) Once the card is read, remove the number from the beginning and append the number  to the end of the random list.

# For the Chance card: (very similar to Community Chest cards)
# a) These work exactly the same as Community Chest cards except that there are 10 cards (1,2,3.....,10) that order a movement. 
# If we draw any other number, we dont move anywhere i.e. we do nothing.

# Track the number landed on the 2 dice each time they are rolled. This number can be used to calculate the probability of landing a sum when 2 dice are rolled. 
# This in turn can be used to check whether our simulation has been truly close to random. (We can easily calculate the probability of getting a specific sum using basic probability).

# How to store the result of each simulation?
# In each simulation:
# 2 Dice are rolled. We will store the sum of the dice. 
# We will store in which square the player finally landed. i.e. We will store the game_board_square_number. 

# once we run the simulation for 1000000 times, we can count the total number of times the each square was  visited and compute the required result.




import math
import time
import random
from  collections import deque
from  collections import Counter



chance_card_deck = deque(random.sample(range(1, 17), 16)) # shuffle the chance card deck before starting the game.
community_chest_card_deck = deque(random.sample(range(1, 17), 16)) # shuffle the chance card deck before starting the game.


# this method returns the  square where the player finally lands after drawing a community chest card. 
def drawACommunityChestCard(token_location):
	advance_to_go = 0 # player lands in "Go" (Square Number: 0)
	go_to_jail = 10  # player lands in "Jail" (Square Number: 10)
	chance_card_dict = {1:advance_to_go, 2:go_to_jail}

	cc_card_drawn = community_chest_card_deck.popleft()
	community_chest_card_deck.append(cc_card_drawn)

	if cc_card_drawn > 2:
		return token_location

	if cc_card_drawn == 1:
		return advance_to_go
	else:
		return go_to_jail




# this method returns the  square where the player finally lands after drawing a chance card. 
def drawAChanceCard(token_location):
	
	global chance_card_deck
	advance_to_go = 0 # player lands in "Go" (Square Number: 00)
	go_to_jail = 10 # player lands in "Jail" (Square Number: 10)
	go_to_c1 = 11 # player lands in "C1" (Square Number: 11)
	go_to_e3 = 24 # player lands in "E3" (Square Number: 24)
	go_to_h2 = 39 # player lands in "H2" (Square Number: 39)
	go_to_r1 = 5 # player lands in "R1" (Square Number: 5)

	chance_card_dict = {1:advance_to_go, 2:go_to_jail, 3:go_to_c1, 4:go_to_e3, 5:go_to_h2, 6:go_to_r1}
	
	# draw a cc card and read the number on it. 
	ch_card_drawn = chance_card_deck.popleft() # get the first card (left most card) from the deck

	# Replace the card to the bottom (right end) of the deck.
	chance_card_deck.append(ch_card_drawn)

	if ch_card_drawn > 10:
		return token_location

	if ch_card_drawn == 1:
		return chance_card_dict[1]
	elif ch_card_drawn == 2:
		return chance_card_dict[2]
	elif ch_card_drawn == 3:
		return chance_card_dict[3]
	elif ch_card_drawn == 4:
		return chance_card_dict[4]
	elif ch_card_drawn == 5:
		return chance_card_dict[5]
	elif ch_card_drawn == 6:
		return chance_card_dict[6]			
	elif ch_card_drawn == 7 or ch_card_drawn == 8:  # player must go to the next railroad company. 
		if token_location == 7:
			return 15  
		elif token_location == 22:
			return 25
		elif token_location == 36:
			return 5
	elif ch_card_drawn == 9: # player must go to the next utility company. 
		if token_location == 7 or token_location == 36:
			return 12
		elif token_location == 22:
			return 28
	elif ch_card_drawn == 10: # go back 3 squares
		return (token_location - 3)				


def simulateMonopoly(n, number_of_sides_of_die):

	community_chest_squares = [2,17,33] 
	chance_squares = [7,22,36]
	go_to_jail = 30 # Square Number 30 == Go to jail
	jail = 10 # Square Number 10 == Jail
	squares_visited_by_the_player = []  # stores the number of the square the player finally landed on in each simulation (turn).
	sum_rolled_on_dice = [] # stores the sum of the dice rolled during each simulation.
	location_of_token = 0 # Token is placed on "Go" (Square Number: 0) at the beginning of the game
	number_of_doubles_rolled = 0
	simulation_number = 0
	
	while (simulation_number < n): # for each simulation
		
		
		dice1 = random.randint(1,number_of_sides_of_die) # roll 2 four-sided dice.
		dice2 = random.randint(1,number_of_sides_of_die)
		roll_dice = dice1 + dice2 # sum of the numbers rolled on both dice.
		

		if dice1 == dice2: # check if you rolled a double
			number_of_doubles_rolled += 1
			if number_of_doubles_rolled == 3: # check if you rolled doubles 3 times in a row
				location_of_token = 10 # land in jail
				number_of_doubles_rolled = 0 # reset the number of times you rolled a double.
				simulation_number += 1	
		
		if (dice1 != dice2) or (number_of_doubles_rolled <= 2) :
			number_of_doubles_rolled = 0
			simulation_number += 1		

		sum_rolled_on_dice.append(roll_dice) # store how much you rolled on the dice. 
		location_of_token += roll_dice # move your token to the square  by the sum of your dice roll. 
		

		if location_of_token > 39:
			location_of_token = location_of_token - 40	
						
		
		if location_of_token in chance_squares: # if you land in chance card square
			location_of_token = drawAChanceCard(location_of_token) # draw a cc card and  move your token  
			

		if location_of_token in community_chest_squares: # if you land in a community chest square
			location_of_token = drawACommunityChestCard(location_of_token) # pick a card from the community chest, move your token and remember what you picked
			

		if 	location_of_token == go_to_jail: # if you land in square number 30, proceed to jail
			location_of_token = jail

		squares_visited_by_the_player.append(location_of_token)	

	# get the top 3 most visited squares:	
	most_visited_squares_counts = Counter(squares_visited_by_the_player).most_common(40)
	print("Most visited Squares",most_visited_squares_counts)
	most_visited_squares = str(most_visited_squares_counts[0][0]) + str(most_visited_squares_counts[1][0]) + str(most_visited_squares_counts[2][0])
	return most_visited_squares



def main():
	start_time = time.time()
	die_side = int(input("Enter number of sides for both die: "))
	print("For a "+str(die_side)+"-sided die: ")
	print ("The six digit modal string is: ", simulateMonopoly(1000000,die_side))
	print ("Problem solved in %s seconds " % (time.time()-start_time))

	

if __name__ == "__main__":
	main()


# Answer: 101524	