from ExpressionTree import ExpressionTree, ExpressionNode

def get_init_state(operand_space):
	forest = []
	for operand in operand_space:
		node = ExpressionNode(operand, False)
		tree = ExpressionTree(
			operand_space=operand_space,
			root_node=node
		)
		forest.append(tree)
	return forest


# Find the next states
def get_next_states(state, operand_space):
	# State must be a single expression tree
	mergeables = get_init_state(operand_space)
	next_states = []
	for other_state in mergeables:
		for operation in ExpressionNode.operations:
			if operation in ExpressionNode.operations_commutative:
				# Commutative operation
				if ExpressionTree.is_merge_valid(operation, state, other_state):
					operation_node = ExpressionNode(operation, True)
					next_states.append(ExpressionTree.merge_trees(operation_node, state, other_state))
				else:
					# Not a commutative operation
					# Order 1
					operation_node = ExpressionNode(operation, True)
					next_states.append(ExpressionTree.merge_trees(operation_node, other_state, state))
					# Order 2
					operation_node = ExpressionNode(operation, True)
					next_states.append(ExpressionTree.merge_trees(operation_node, other_state, state))
	return next_states	


def is_operand_space_exhausted(state):
	return all(state.bitmask)

def is_goal_reached(state, goal_value):
	return is_operand_space_exhausted(state) and state.evaluation==goal_value


"""
# Testing state generation
sample_state = [4, 5, 6, 3, 4, 5, 6, 5]
sample_state = [1, 5, 7, 2, 3, 3, 6, 4]
print(get_next_states(sample_state))
"""

