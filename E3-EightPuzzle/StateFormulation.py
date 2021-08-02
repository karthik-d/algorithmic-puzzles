INITIAL_STATE = (
	(7, 2, 4),
	(5, 0, 6),
	(8, 3, 1),
)

GOAL_STATE = (
	(0, 1, 2),
	(3, 4, 5),
	(6, 7, 8),
)

NUM_ROWS = len(INITIAL_STATE)
NUM_COLS = len(INITIAL_STATE[0])


def get_next_states(state):
	# Swap 0 with any of its neighbors

	def locate_empty_space():
		for i in range(NUM_ROWS):
			for j in range(NUM_COLS):
				if state[i][j] == 0:
					return i,j

	def make_state(initial, final):
		# By moving 0 from initial to final
		new_state = [list(row) for row in state]
		new_state[initial[0]][initial[1]] = state[final[0]][final[1]]
		new_state[final[0]][final[1]] = 0
		new_state = tuple(map(tuple, new_state))
		return new_state

	result = list()
	row, col = locate_empty_space()
	
	# Move left
	if (col-1)>-1:
		result.append(make_state((row, col), (row, col-1)))
	# Move right
	if (col+1)<NUM_COLS:
		result.append(make_state((row, col), (row, col+1)))

	# Move up
	if (row-1)>-1:
		result.append(make_state((row, col), (row-1, col)))
	# Move down
	if (row+1)<NUM_ROWS:
		result.append(make_state((row, col), (row+1, col)))
	
	return result

'''
# Checking the next state generation function
for state in get_next_states(INITIAL_STATE):
	for row in state:
		print(row)
	print()
'''

def goal_test(state):
	for i in range(NUM_ROWS):
		for j in range(NUM_COLS):
			if state[i][j] != GOAL_STATE[i][j]:
				return False 
	return True			


# Compare the current state of `this` direction search
# to the fringe states of `that` direction search
def intersection_test(this_state, that_fringe):
	
	def are_states_same(state_A, state_B):
		for i in range(NUM_ROWS):
			for j in range(NUM_COLS):
				if state_A[i][j] != state_B[i][j]:
					return False 
		return True 
	
	for state in that_fringe:
		if are_states_same(state, this_state):
			return True
	return False