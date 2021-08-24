from Queue import Queue 

from StateFormulation import *


def deduce_path(state, parents):
	
	def deduce_BFS_path_rec(state, path_seq):
		this_parent = parents[state]
		if this_parent is None:
			return path_seq
		path_seq = [this_parent] + path_seq[:]
		return deduce_BFS_path_rec(this_parent, path_seq)
	
	return deduce_BFS_path_rec(state, [])


def search():
	polygons = [
		Polygon([(1,1), (1,3), (4,3), (4,1)]),
		Polygon([(5,2), (6,4), (4,5)])
	]
	state_space = StateSpace(
		start = (0,0),
		end = (6,5),
		obstacles = polygons
	)
	queue = Queue([state_space.start])
	explored_states = set()
	parents = {1: None}

	# Store the dequeued node count
	node_count = 0
	# Store the last node number of levels
	level_limits = Queue([1, 1])
	while(not queue.is_empty()):
		state = queue.dequeue()
		print(state)
		node_count += 1
		if state_space.is_visited(state):
			continue
		state_space.move_to_state(state)
		"""
		if goal_test(state):
			return explored_states, parents
		"""
		# Find fringe and add to queue
		# Add fringe size to current level's limit
		fringe = state_space.get_next_states(include_visited=False)
		queue.enqueue(fringe)
		print("FRINGE", fringe)
		level_limits.set_back(level_limits.get_back() + len(fringe))
		# Check if current level has reached its end
		if node_count == level_limits.get_front():
			print("LEVEL-CHANGE")
			# Remove terminated level's end
			# Duplicate next level's limit to store next level limit
			level_limits.dequeue()
			level_limits.enqueue([level_limits.get_back()])
	
	return False 

search()
