from Queue import Queue 
from copy import deepcopy

from StateFormulation import *
from search_utils import *


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


"""
polygons = [
	Polygon([(5,2), (6,4), (4,5)]),
	Polygon([(1,1), (1,3), (4,3), (4,1)]),
]
"""

polygons = [
	Polygon([(220,616), (220,666), (251,670), (272,647)]),
	Polygon([(341,655), (359,667), (374,651), (366,577)]),
	Polygon([(311,530), (311,559), (339,578), (361,560), (361, 528), (336, 516)]),
	Polygon([(105,628), (151,670), (180,629), (156,577), (113, 587)]),
	Polygon([(118,517), (245,517), (245,577), (118,557)]),
	Polygon([(280,583), (333,583), (333,665), (280,665)]),
	Polygon([(252,594), (290,562), (264,538)]),
	Polygon([(198,635), (217,574), (182,574)]),
]

state_space = StateSpace(
	start = (120,650),
	end = (380,560),
	obstacles = polygons
)
print(search(state_space))

# Solution Found
# (120,650), (105,628), (118,517), (336,516), (361,528), (380,560)
# Cost: 421.3344534244741