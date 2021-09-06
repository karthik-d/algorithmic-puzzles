import numpy.random as random
from copy import deepcopy

NUM_QUEENS = 8
MAX_POSSIBLE_ATTACKS =  ( NUM_QUEENS * (NUM_QUEENS-1) ) // 2  # i.e nC2

def generate_random_state():
	state = [[
		random.randint(0, NUM_QUEENS)
		for x in range(NUM_QUEENS)
	]]
	return state


def count_attacks(state):
	num_attacks = 0
	# Count for each queen
	for column in range(NUM_QUEENS):
		# Count queens in same row. Exclude self
		num_attacks += state.count(state[column])-1
		# Try right and left diagonals. Exclude self
		num_attacks -= 2
		diag_sum = column + state[column]
		diag_diff = column - state[column]
		for i in range(NUM_QUEENS):
			if i+state[i]==diag_sum:
				num_attacks += 1
			if i-state[i]==diag_diff:
				num_attacks += 1
	# Each pair-attack was counted twice. Hence, return result/2
	return num_attacks//2			


# Find the next states
def get_next_states(state):
	moves = list()
	attacks = list()
	# Try moving each queen to every other position in its column
	for column in range(NUM_QUEENS):
		for row in range(NUM_QUEENS):
			if row == state[column]:
				# If moving again to same row, skip
				continue
			else:
				moves.append((column, row))
				temp_state = deepcopy(state)
				temp_state[column] = row
				attacks.append(count_attacks(temp_state))
	return moves, attacks


# Find the lowest attack suuccessor state
def get_next_best_move(state):
	min_attacks = MAX_POSSIBLE_ATTACKS
	min_attacks_move = None
	# Try moving each queen to every other position in its column
	for column in range(NUM_QUEENS):
		for row in range(NUM_QUEENS):
			if row == state[column]:
				# If moving again to same row, skip
				continue
			temp_state = deepcopy(state)
			temp_state[column] = row
			num_attacks = count_attacks(temp_state)
			if num_attacks<min_attacks:
				min_attacks_move = (column, row)
				min_attacks = num_attacks 
	# Return the best move and its cost value
	return min_attacks_move, min_attacks

sample_state = [4, 5, 6, 3, 4, 5, 6, 5]
print(get_next_states(sample_state))
