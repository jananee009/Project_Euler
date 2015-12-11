# Monopoly Odds
# Problem Source: https://projecteuler.net/problem=84
# Approach: 1. There are 2 ways to solve the problem. a) Using probability and numbers b) Using Monte Carlo Simulation.
# If we use Monte Carlo Simulation, we need to set up the problem such that we can simulate it for say atleast 1 million times.


# Data Structures needed:
# A list (of length 40) to store all the squares on the monopoly game board.
# A list (of length 10) to maintain the "Chance" cards.
# A list (of length 2) to maintain "Community Chest " cards.
# A list (of length 1000000) to keep track of which square the player landed on, ultimately, at the end of every turn. 



# Things to do:
# Simulate the roll of 2 6-sided dice atleast a million times.
# For the Community Chest card: 
# a) For the first time, randomly generate one of the 2 numbers (1,2). Subsequently, each number should be picked alternately. 
# b) For e.g. suppose, first time, randomly we pick number 1 (and the corresponding CC card). Then the subsequent choices of cc card must be (2,1,2,1,2,1,2,.......)
# For the Chance card: 
# a) There are 10 chance cards. First generate a random list of 10 numbers containing numbers (1,2,3,.....,10). 
# b) Then each time the player lands on the Chance square, get the first number (and the corresponding chance card) from the beginning of the random list. 
# c) Once the card is read, remove the number from the beginning and append the number  to the end of the random list. 
# Track the number landed on the 2 dice each time they are rolled. This number can be used to calculate the probability of landing a sum when 2 dice are rolled. 
# This in turn can be used to check whether our simulation has been truly close to random. (We can easily calculate the probability of getting a specific sum using basic probability).

# How to store the result of each simulation?
# In each simulation:
# 2 Dice are rolled. We will store the sum of the dice. 
# We will store in which square the player utimately landed. i.e. We will store the game_board_square_number. 
# We will store how many times the player landed on community chest / chance cards in the form (i,game_board_square_number), where i == simulation number

# once we run the simulation for 1000000 times, we can count the total number of times the each square was ultimately visited and compute the probability.

# Game Rules:


import math
import time
import random
from  collections import deque
from  collections import Counter



chance_card_deck = deque(random.sample(range(1, 11), 10))

# this method returns the ultimate square where the player lands after drawing and reading a community card. 
def drawACommunityChestCard(last_drawn_cc_card_num):
	advance_to_go = 0 # 0 is the square number where the player will ultimately land.
	go_to_jail = 10  # player lands in "Jail" (Square Number: 10)
	community_chest_card_dict = {1:advance_to_go, 2:go_to_jail}

	if last_drawn_cc_card_num == 1:
		current_draw = 2
		return (current_draw,community_chest_card_dict[2])
	elif last_drawn_cc_card_num == 2:
		current_draw = 1
		return (current_draw,community_chest_card_dict[1])
	else:
		current_draw = random.randint(1,2)	
		return (current_draw,community_chest_card_dict[current_draw])	


# this method returns the ultimate square where the player lands after drawing a chance card. 
def drawAChanceCard(token_location):
	
	advance_to_go = 0 # player lands in "Go" (Square Number: 00)
	go_to_jail = 10 # player lands in "Jail" (Square Number: 10)
	go_to_c1 = 11 # player lands in "C1" (Square Number: 11)
	go_to_e3 = 24 # player lands in "E3" (Square Number: 24)
	go_to_h2 = 39 # player lands in "H2" (Square Number: 39)
	go_to_r1 = 5 # player lands in "R1" (Square Number: 5)

	chance_card_dict = {1:advance_to_go, 2:go_to_jail, 3:go_to_c1, 4:go_to_e3, 5:go_to_h2, 6:go_to_r1, 7:"go_to_next_r", 8:"go_to_next_r", 9:"go_to_next_u", 10:"go_back_3_squares"}
	
	# draw a cc card and read the number on it. 
	cc_card_drawn = chance_card_deck.popleft() # get the first card (left most card) from the deck

	# add the card to the bottom (right end) of the deck.
	chance_card_deck.append(cc_card_drawn)

	if cc_card_drawn == 1:
		return chance_card_dict[1]
	elif cc_card_drawn == 2:
		return chance_card_dict[2]
	elif cc_card_drawn == 3:
		return chance_card_dict[3]
	elif cc_card_drawn == 4:
		return chance_card_dict[4]
	elif cc_card_drawn == 5:
		return chance_card_dict[5]
	elif cc_card_drawn == 6:
		return chance_card_dict[6]			
	elif cc_card_drawn == 7 or 8:
		if token_location == 7:
			return 15  # player must go to the nearest railroad. 
		elif token_location == 22:
			return 25
		elif token_location == 36:
			return 5
	elif cc_card_drawn == 9:
		if token_location == 7 or 36:
			return 12
		elif token_location == 22:
			return 28
	elif cc_card_drawn == 10: # go back 3 squares
		return (token_location - 3)
				



def simulateMonopoly(n):

	community_chest_squares = [2,17,33] 
	chance_squares = [7,22,36]

	squares_visited_by_the_player = []  # stores the number of the square the player ultimately landed on in each simulation (turn).
	sum_rolled_on_dice = [] # stores the sum of the dice rolled during each simulation.
	landed_on_cc_or_ch = [] # stores a tuples of the form (simulation_no, square_number_of_cc_or_ch)
	location_of_token = 0 # corresponds to the "go" square on the game board.
	last_cc_card_drawn = 0 # initial value

	for i in range(1,n+1): # for each simulation
		
		roll_dice = random.randint(1,6) + random.randint(1,6) # first roll the dice
		sum_rolled_on_dice.append(roll_dice) # store the result. 
		location_of_token += roll_dice # move your token to the square given by the sum of your dice roll. 
		location_of_token = location_of_token % 40: 
						
		
		if location_of_token in chance_squares:
			landed_on_cc_or_ch.append((i,location_of_token))
			location_of_token = drawAChanceCard(location_of_token)

		if location_of_token in community_chest_squares: # if you land in a community chest square
			landed_on_cc_or_ch.append((i,location_of_token)) # store how you landed there
			last_cc_card_drawn , location_of_token = drawACommunityChestCard(last_cc_card_drawn) # pick a card from the community chest, move your token and remember what you picked
	

		squares_visited_by_the_player.append(location_of_token)	

	# get the top 3 most visited squares:	
	most_visited = Counter(squares_visited_by_the_player).most_common(3)
	print most_visited

	wrong_values = [square_num for square_num in squares_visited_by_the_player if square_num > 39]
	print "wrong_values: ",wrong_values
	return



def main():
	start_time = time.time()
	simulateMonopoly(1000000)
	print"Problem solved in %s seconds " % (time.time()-start_time)

	

if __name__ == "__main__":
	main()


# Answer: 	