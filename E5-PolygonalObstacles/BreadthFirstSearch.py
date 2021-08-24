from Queue import Queue 

from StateFormulation import (
	get_next_states,
	goal_test,
	INITIAL_STATE,
	GOAL_STATE,
	NUM_ROWS,
	NUM_COLS
)


def deduce_path(state, parents):
	
	def deduce_BFS_path_rec(state, path_seq):
		this_parent = parents[state]
		if this_parent is None:
			return path_seq
		path_seq = [this_parent] + path_seq[:]
		return deduce_BFS_path_rec(this_parent, path_seq)
	
	return deduce_BFS_path_rec(state, [])


def search():

	state_space = Queue([INITIAL_STATE])
	explored_states = set()
	parents = {INITIAL_STATE: None}

	while(not state_space.is_empty()):
		state = state_space.dequeue()
		if state in explored_states:
			continue
		explored_states.add(state)
		if goal_test(state):
			return explored_states, parents
		fringe = get_next_states(state)
		state_space.enqueue(fringe)
		for new_state in fringe:
			if new_state not in parents:
				parents[new_state] = state
	
	return False 
