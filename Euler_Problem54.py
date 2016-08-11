# Poker hands
# Problem Source: https://projecteuler.net/problem=54
# Poker Hand Rank is as follows:
# High Card: Highest value card. Strength Rank = 1. 
# One Pair: Two cards of the same value. Strength Rank = 2.
# Two Pairs: Two different pairs. Strength Rank = 3.
# Three of a Kind: Three cards of the same value. Strength Rank = 4.
# Straight: All cards are consecutive values. Strength Rank = 5.
# Flush: All cards of the same suit. Strength Rank = 6.
# Full House: Three of a kind and a pair. Strength Rank = 7.
# Four of a Kind: Four cards of the same value. Strength Rank = 8.
# Straight Flush: All cards are consecutive values of same suit. Strength Rank = 9.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. Strength Rank = 10




import math
import time
import random


def readAndStoreEachcard(hand):
	ranks_suits = [n for n in range(2,15)] + list('CDHS')
	countDict = {n:0 for n in ranks_suits}
	for card in hand:
		rank = card[0]
		suit = card[1]
		if rank.isdigit():
			countDict[int(rank)] += 1
		else:
			if rank == "T":
				countDict[10] += 1
			elif rank == "J":
				countDict[11] += 1
			elif rank == "Q":
				countDict[12] += 1
			elif rank == "K":
				countDict[13] += 1
			elif rank == "A":
				countDict[14] += 1				

		countDict[suit] += 1	
	return countDict

def isSequentialList(inputList):
	print "inputList: ",inputList
	temp = [n for n in range(inputList[0],inputList[-1]+1)]

	if temp == inputList:
		return True

	return False	


def determineHandStrength(player_hand_count):
	
	pairs = 0
	three_of_a_kind = False
	four_of_a_kind = False
	same_suit = False
	card_ranks = []

	print "player_hand_count :", player_hand_count

	for key, value in player_hand_count.iteritems():

		if value > 0:
		
			if isinstance(key, int) : # checking only ranks
				
				card_ranks.append(key)

				if value == 2: 
					# we have a pair
					pairs += 1

				elif value == 3:
					three_of_a_kind = True

				elif value == 4:
					four_of_a_kind = True

			else: # checking suits
				if value == 5:
					# all 5 cards belong to same suit. So, we have either a Royal flush, Straight flush or plain flush.
					same_suit = True 


	print "card_ranks: ",card_ranks	

	# determine the handstrength			
	if pairs == 1:
		if 	three_of_a_kind:
			# we have a full house here.
			handStrength = 7
		else:
			# We have 1 pair. 
			handStrength = 2

	elif pairs == 2:
		# We have 2 pairs
		handStrength = 3

	elif three_of_a_kind:
		# We have a three of a kind.
		handStrength = 4

	elif four_of_a_kind:
		# We have a 4 of a kind. 
		handStrength = 8	
		
	elif (isSequentialList(card_ranks.sort())): 
		# cards are in sequence
		if same_suit:
			if card_ranks == [10,11,12,13,14]:
				# We have a royal flush.
				handStrength = 10
			else:
				# We have a straight flush
				handStrength = 9
		else:
			# cards are sequential, but they dont belong to the same suit. Hence we have a straight.
			handStrength = 5		
	elif same_suit:
		# cards belong to same suit, but they are not in sequence. Hence it is a flush.
		handStrength = 6
	else: 
		handStrength = 1

	return ( handStrength, card_ranks )	
			
			
			
		 								


		

	return hsRank	

def determineWinner():
	
	#player1_Hands = BothplayerPokerHands[0]
	#player2_Hands = BothplayerPokerHands[1]

	player1_Hands = [["2D", "9C", "AS", "AH", "AC"]]
	player2_Hands = [["3D", "6D", "7D", "TD", "QD"]]

	# number of hands won by each player
	player1 = 0
	player2 = 0

	
	

	for i  in range(0,len(player1_Hands)):
		player_1_hand = player1_Hands[i]
		player_2_hand = player2_Hands[i]

		# read each card and store rank and suit
		player1_hand_count = readAndStoreEachcard(player_1_hand)
		player2_hand_count = readAndStoreEachcard(player_2_hand)

		# determine hand strength for player 1:
		player1_hand_rank, player1_cards = determineHandStrength(player1_hand_count)
		print "player1_hand_rank: ",player1_hand_rank

		player2_hand_rank, player2_cards = determineHandStrength(player2_hand_count)
		print "player2_hand_rank: ",player1_hand_rank

		if player1_hand_rank > player2_hand_rank:
			player1 += 1
		elif player1_hand_rank < player2_hand_rank:	
			player2 += 1
		else: # There is a tie
			print "There is a tie."
			'''
			if player1_hand_rank == 9: # or player2_hand_rank == 9
				for r1, r2 in zip(player1_cards().sort(reverse = True), player2_cards.sort(reverse = True)):
					if r1 == r2:
						continue
					elif r1 > r2:
						player1 += 1
						break
					else:
						player2 += 1
						break

			'''

	print "Player_1: ",	player1
	print "player_2: ", player2

	return					
							



def readAllPokerHands():
	player1_hands = []
	player2_hands = []
	f = open('p054_poker.txt','rU')
	
	for line in f:	
		p1 = []
		p2 = []
		hands = line.split(" ")

		# player 1 hands
		for j in range(0,5):
			p1.append(hands[j])
		player1_hands.append(p1)

		# player 2 hands
		for j in range(5,10):
			p2.append(hands[j])
		player2_hands.append(p2)					
	f.close()
	return (player1_hands,player2_hands)
	

def main():
	start_time = time.time()
	#pokerHands = readAllPokerHands() # read all the numbers in a grid in to a matrix.
	determineWinner()
	#print determineWinner(pokerHands)
	print "Solution found in" , (time.time()-start_time), "seconds."



if __name__ == "__main__":
	main()


# Answer: 