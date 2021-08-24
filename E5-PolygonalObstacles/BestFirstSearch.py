from PriorityQueue import PriorityQueue 
from copy import deepcopy

from StateFormulation import *
from search_utils import *

def deduce_path(state, parents):
	
	def deduce_BFS_path_rec(state, path_seq):
		this_parent = parents[state]
		if this_parent is None:
			return path_seq
		path_seq = [this_parent] + path_seq[:]
		return deduce_BFS_path_rec(this_parent, path_seq)
	
	return deduce_BFS_path_rec(state, [])


def search(state_space):

	# Queue of fringe states and their respective paths
	state_queue = Queue([state_space.start])
	path_queue = Queue([Path([state_space.start])])
	while(not state_queue.is_empty()):
		# PRE-VISIT
		state = state_queue.dequeue()
		path_to_state = path_queue.dequeue()	
		if state_space.is_visited(state):
			continue
		# VISIT		
		# Move to state and do goal test
		state_space.move_to_state(state)
		if state_space.at_goal_state():
			return path_to_state
		# POST-VISIT
		# Find fringe and add to queue
		fringe = state_space.get_next_states(include_visited=False)
		state_queue.enqueue(fringe)
		# Store paths to each fringe
		for next_state in fringe:
			next_path = deepcopy(path_to_state)
			next_path.add_state(next_state)
			path_queue.enqueue([next_path])
	
	return False 


polygons = [
	Polygon([(1,1), (1,3), (4,3), (4,1)]),
	Polygon([(5,2), (6,4), (4,5)])
]
state_space = StateSpace(
	start = (0,0),
	end = (6,5),
	obstacles = polygons
)
print(search(state_space))
