import numpy.random as random
from copy import deepcopy

NUM_QUEENS = 8
MAX_POSSIBLE_ATTACKS =  ( NUM_QUEENS * (NUM_QUEENS-1) ) // 2  # i.e nC2
MIN_POSSIBLE_ATTACKS = 0

def generate_random_state():
	state = [
		random.randint(0, NUM_QUEENS)
		for x in range(NUM_QUEENS)
	]
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
	
	
def count_non_attacks(state):
	return MAX_POSSIBLE_ATTACKS - count_attacks(state)		


# Find the next states
def get_next_states(state):
	moves = list()
	attacks = list()
	disp_arr = [[None for x in range(NUM_QUEENS)] for y in range(NUM_QUEENS) ]
	# Try moving each queen to every other position in its column
	for column in range(NUM_QUEENS):
		for row in range(NUM_QUEENS):
			if row == state[column]:
				# If moving again to same row, skip
				disp_arr[row][column] = 'Q '
				continue
			else:
				temp_state = deepcopy(state)
				temp_state[column] = row
				disp_arr[row][column] = str(count_non_attacks(temp_state)).ljust(2)
	for i in disp_arr:
		print(i)
	return moves, attacks
	

def is_goal_reached(state):
	return count_attacks(state)==0
	

# Display the state, visually
def display_state(state):
	disp_array = [
		[ 'Q' if state[col]==row else '-' for row in range(NUM_QUEENS) ]
		for col in range(NUM_QUEENS)
	]
	for disp_row in disp_array:
		print(disp_row)


"""
# Testing state generation
sample_state = [4, 5, 6, 3, 4, 5, 6, 5]
sample_state = [1, 5, 7, 2, 3, 3, 6, 4]
print(get_next_states(sample_state))
"""

