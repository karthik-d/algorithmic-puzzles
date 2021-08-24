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

	queue = StateSpace(
		start = (0,0),
		end = (6,5),
		obstacles = polygons
	)
	queue = Queue([states_space.start])

	explored_states = set()
	parents = {INITIAL_STATE: None}

	
	while(not queue.is_empty()):
		state = queue.dequeue()
		if state_space.is_visited(state):
			continue
		state_space.move_to_state(state)
		explored_states.add(state)
		if goal_test(state):
			return explored_states, parents
		fringe = state_space.get_next_states(include_visited=False)
		queue.enqueue(fringe)
	
	return False 
