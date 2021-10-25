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

	def get_bitmask(self, value, operand_space):
		return [ operand==x for x in operand_space ]



class ExpressionTree:

	"""
	Nodes represent sequence of numbers (tree-structure)
	Edges represent an operation (+, -, *, /)
	"""

	def __init__(self, operand_space, bitmask, root):
		self.operand_space = operand_space
		self.bitmask = bitmask
		self.root = root

	@classmethod
	def merge_bitmasks(self, bitmask_1, bitmask_2):
		return [ x or y for x,y in zip(bitmask_1, bitmask_2) ]

	@classmethod
	def get_bitmask(self, operand):
		return [ operand==x for x in self.operand_space ]

	@classmethod
	def is_merge_valid(cls, lhs, rhs):
		if lhs.operand_space != rhs.operand_space:
			return False 
		# NAND-operation
		# Same operand must NOT have been used in both already
		for x_bit, y_bit in zip(lhs.bitmask, rhs.bitmask):
			if x_bit and y_bit:
				return False 
		return True

	@classmethod
	def merge_trees(cls, operation_node, lhs, rhs):
		""" 
		lhs, rhs are trees
		"""
		# Ensure the nodes can be merged
		assert is_merge_valid(lhs, rhs) == True
		# Merge nodes
		operation_node.left_child = lhs.root
		operation_node.right_child = rhs.root
		# Make new tree
		new_tree = ExpressionTree(
			operand_space=lhs.operand_space,
			bitmask=cls.merge_bitmasks(lhs.bitmask, rhs.bitmask),
			root=operation_node
		)
		return new_tree
		
		