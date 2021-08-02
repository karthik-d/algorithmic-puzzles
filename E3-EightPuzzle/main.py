from copy import deepcopy

INITIAL_STATE = [
	[7, 2, 4],
	[5, 0, 6],
	[8, 3, 1],
]

GOAL_STATE = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
]

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
		new_state = deepcopy(state)
		new_state[initial[0]][initial[1]] = state[final[0]][final[1]]
		new_state[final[0]][final[1]] = 0
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

for state in get_next_states(INITIAL_STATE):
	for row in state:
		print(row)
	print()