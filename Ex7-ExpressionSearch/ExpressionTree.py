from copy import deepcopy

class ExpressionNode:

	operations = [ '+', '-', '*', '/' ]
	operations_commutative = ['+', '*']

	def __init__(self, value, assert_operation=True):
		self.is_operand = value not in self.operations
		if assert_operation:
			assert self.is_operand == False
		# Set node values
		self.value = value
		self.left_child = None 
		self.right_child = None 

	def get_bitmask(self, value, operand_space):
		return [ operand==x for x in operand_space ]



class ExpressionTree:

	"""
	Nodes represent sequence of numbers (tree-structure)
	Edges represent an operation (+, -, *, /)
	"""

	def __init__(self, operand_space, root_node, bitmask=None, evaluation=None):
		"""
		For constructing trees from scratch, root_node is assumed to be a single node
		Bitmask is computed. Expression result is computed
		For constructing trees from two other trees, bitmask must be supplied through the merge
		operation. Expression evaluation must be passed
		"""
		self.operand_space = operand_space
		self.root = root_node
		# Bitmask set
		if bitmask is None:
			self.bitmask = self.get_bitmask(self.root)
		else:
			self.bitmask = bitmask
		# Evaluation result
		if evaluation is None:
			self.evaluation = self.root.value 
		else:
			self.evaluation = evaluation

	def display(self):
		display_queue = [self.root]
		while display_queue:
			node = display_queue.pop(0)
			print(node.value)
			if node.left_child is not None:
				display_queue.append(node.left_child)
			if node.right_child is not None:
				display_queue.append(node.right_child)	

	def get_bitmask(self, operand_node):
		return [ operand_node.value==x for x in self.operand_space ]

	@classmethod
	def merge_bitmasks(cls, bitmask_1, bitmask_2):
		return [ x or y for x,y in zip(bitmask_1, bitmask_2) ]

	@classmethod 
	def evaluate(cls, operation, lhs, rhs):
		if operation == '+':
			return lhs + rhs 
		elif operation == '-':
			return lhs - rhs 
		elif operation == '*':
			return lhs * rhs 
		elif operation == '/':
			return lhs // rhs

	@classmethod
	def is_merge_valid(cls, operation, lhs, rhs):
		if operation == '/' and lhs.evaluation % rhs.evaluation != 0:
			# print("F1")
			return False
		if lhs.operand_space != rhs.operand_space:
			# print("F2")
			return False 
		# NAND-operation
		# Same operand must NOT have been used in both already
		for x_bit, y_bit in zip(lhs.bitmask, rhs.bitmask):
			if x_bit and y_bit:
				# print("F3")
				return False 
		return True

	@classmethod
	def merge_trees(cls, operation_node, lhs, rhs):
		""" 
		lhs, rhs are trees
		"""
		# Ensure the nodes can be merged
		assert cls.is_merge_valid(operation_node.value, lhs, rhs) == True
		# Merge nodes
		operation_node.left_child = lhs.root
		operation_node.right_child = rhs.root
		# Make new tree
		lhs = deepcopy(lhs)
		rhs = deepcopy(rhs)
		new_tree = ExpressionTree(
			operand_space=lhs.operand_space,
			root_node=operation_node,
			bitmask=cls.merge_bitmasks(lhs.bitmask, rhs.bitmask),
			evaluation=cls.evaluate(operation_node.value, lhs.evaluation, rhs.evaluation)
		)
		return new_tree

"""		
def run_test():
	operands = [1, 2, 3, 5]
	root_node = ExpressionNode(5, False)
	tree_1 = ExpressionTree(
		operands,
		root_node
	)
	root_node = ExpressionNode(1, False)
	tree_2 = ExpressionTree(
		operands,
		root_node
	)
	operation = ExpressionNode('+', True)
	tree = ExpressionTree.merge_trees(operation, tree_1, tree_2)
	tree.display() 
	print(operands)
	print(tree.bitmask)
	print(tree.evaluation)

run_test()
"""