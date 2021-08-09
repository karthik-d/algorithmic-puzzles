from Stack import *
from StateFunctions import *


line = "----------------------------"


def deduce_path(state, parents):
	
	def deduce_path_rec(state, path_seq):
		this_parent = parents[state]
		# Reached the root node
		if this_parent is None:
			return path_seq
		# Prepend node
		path_seq = [this_parent] + path_seq[:]
		return deduce_path_rec(this_parent, path_seq)

	return deduce_path_rec(state, [])


def DFS():

	state_space = Stack([INITIAL_STATE])
	goal_states = list()
	explored_states = set()
	parents = {INITIAL_STATE: None}

	while not state_space.is_empty():
		# Get next state and its path
		state = state_space.pop()
		# Skip iteration if state already explored
		if state in explored_states:
			continue
		explored_states.add(state)
		# Check if the state is a goal-state
		if is_goal_state(state):
			goal_states.append(state)
		# Find the next states
		fringe = get_next_states(state)
		state_space.push(fringe)
		# Add parent of each fringe state, if not already added
		for new_state in fringe:
			if new_state not in parents:
				parents[new_state] = state 

	return goal_states, explored_states, parents 


if __name__ == '__main__':

	goal_states, explored_states, parents = DFS()
	print(parents)

	print("\nDISTINCT EXPLORED STATES COUNT: ", len(explored_states))

	print("\nGOAL STATES COUNT: ", len(goal_states))

	print("\nINITIAL STATE")
	print(INITIAL_STATE)

	print("\nGOAL STATES")
	for state in goal_states:
		print(state)

	print("\nEXPLORED STATES")
	for state in explored_states:
		print(state)

	for state in goal_states:
		print("\nPATH to reach", state)
		print("\n".join(map(str, deduce_path(state, parents))))
		print(state, '--> GOAL STATE')

            