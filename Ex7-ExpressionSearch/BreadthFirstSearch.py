from Queue import Queue 
from numpy import inf
from copy import deepcopy

from StateFormulation import *


def search(operand_space, goal_value):

	# Queue of fringe states and their respective paths
	state_queue = Queue(get_init_state(operand_space))
	# Node Counters
	visited_cnt = 0
	generated_cnt = 0
	closest_result = ExpressionTree(
		operand_space=operand_space,
		root_node=ExpressionNode(inf, False),
		bitmask=[],
		evaluation=inf
	)
	while(not state_queue.is_empty()):
		# PRE-VISIT
		state = state_queue.dequeue()
		# VISIT		
		if is_operand_space_exhausted(state):
			best_diff = abs(goal_value-closest_result.evaluation)
			curr_diff = abs(goal_value-state.evaluation)
			if curr_diff == 0:
				# Goal hit
				return state 
			elif curr_diff < best_diff:
				# New nearer state
				closest_result = deepcopy(state)
		# POST-VISIT
		# Find fringe and add to queue
		fringe = get_next_states(state, operand_space)
		state_queue.enqueue(fringe)
	
	if closest_result.evaluation == inf:
		return False
	else:
		return closest_result

"""
search(
	operand_space=[4, 8, 9],
	goal_value=18
).display()
"""


