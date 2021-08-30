import np.random as random
from copy import deepcopy

NUM_QUEENS = 8

def generate_random_state():
	state = [[
		random.randint(0, NUM_QUEENS)
		for x in range(NUM_QUEENS)
	]]
	return state

INITIAL_STATE = generate_random_state()


def count_attacks(state):
	num_attacks = 0
	# Count for each queen
	for column in range(NUM_QUEENS):
		# Count queens in same row. Exclude self
		num_attacks += state.count(state[column])-1
		# Try right diagonal


# Find the next states
def get_next_states(state):
	moves = list()
	attacks = list()
	for column in range(NUM_QUEENS):
		for row in range(NUM_QUEENS):
			if row == state[column]:
				continue
			else:
				moves.append((column, row))
				temp_state = deepcopy(state)
				temp_state[column] = row
				attacks.append(count_attacks(temp_state))
	return moves, attacks
