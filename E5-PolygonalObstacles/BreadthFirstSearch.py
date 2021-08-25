from Queue import Queue 
from copy import deepcopy

from StateFormulation import *
from search_utils import *


def search(state_space):

	# Queue of fringe states and their respective paths
	state_queue = Queue([state_space.start])
	path_queue = Queue([Path([state_space.start])])
	# Node Counters
	visited_cnt = 0
	generated_cnt = 0
	while(not state_queue.is_empty()):
		# PRE-VISIT
		state = state_queue.dequeue()
		path_to_state = path_queue.dequeue()	
		if state_space.is_visited(state):
			continue
		# VISIT		
		# Move to state and do goal test
		state_space.move_to_state(state)
		visited_cnt += 1
		if state_space.at_goal_state():
			return path_to_state, generated_cnt, visited_cnt
		# POST-VISIT
		# Find fringe and add to queue
		fringe = state_space.get_next_states(include_visited=False)
		state_queue.enqueue(fringe)
		# Store paths to each fringe
		for next_state in fringe:
			next_path = deepcopy(path_to_state)
			next_path.add_state(next_state)
			path_queue.enqueue([next_path])
		generated_cnt += len(fringe)
	
	return False 


"""
polygons = [
	Polygon([(5,2), (6,4), (4,5)]),
	Polygon([(1,1), (1,3), (4,3), (4,1)]),
]
"""
# Solution Found
# (120,650), (105,628), (118,517), (336,516), (361,528), (380,560)
# Cost: 421.3344534244741