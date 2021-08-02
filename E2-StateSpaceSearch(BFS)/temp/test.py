from StateFunctions import *
from Queue import *

state_space = Queue([INITIAL_STATE])
explored_states = list()

while not state_space.is_empty():
	# Get next state and its path
	state = state_space.dequeue()
	if state in explored_states:
		print("Skipping", state)
		continue
	explored_states.append(state)
	fringe = get_next_states(state)
	state_space.enqueue(fringe)
	print(state)
	print(fringe)
	input()