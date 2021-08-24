class Path:

	def __init__(self, sequence=[], cost=0):
		self.sequence = sequence
		self.cost = cost

	def add_state(self, state):
		self.cost += self.sequence[-1].distance_to(state)
		self.sequence.append(state)

	def __str__(self):
		return " -> ".join(map(str, self.sequence))+'\nCost: {cost}'.format(cost=self.cost)