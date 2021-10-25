class ExpressionNode:

	operations = [ '+', '-', '*', '/' ]

	def __init__(self, value, assert_operation=True):
		self.is_operand = value not in operations
		if assert_operation:
			assert self.is_operand == False
		# Set node values
		self.value = value
		self.left_child = None 
		self.right_child = None


class ExpressionTree:

	"""
	Nodes represent sequence of numbers (tree-structure)
	Edges represent an operation (+, -, *, /)
	"""

	def __init__(self, operand_space):
		self.operand_space = operand_space
		self.bitmask = [ False for _ in operand_space ]
		self.root = None

	def get_bitmask(self, operand):
		return [ operand==x for x in self.operand_space ]

	def check_merge_valid()

	@classmethod
	def merge_trees(cls, operation_node, lhs, rhs):
		""" 
		lhs, rhs are trees
		"""
		# Merge nodes
		operation_node.left_child = lhs.root
		operation_node.right_child = rhs.root
		# Make new tree
		new_tree = ExpressionTree(self.operand_space)
		new_tree.root = operation_node
		return new_tree
		
		