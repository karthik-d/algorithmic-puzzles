class PriorityQueue:

	def __init__(self, priority_func):
		self.elements = []
		self.size = 0
		self.priority_func = priority_func
	
	def enqueue(self, insertion_list):
		insertion_list.sort()
		# Merge elements
		a_ctr = 0
		b_ctr = 0
		new_list = []
		while a_ctr<self.size and b_ctr<len(insertion_list):
			# Small Number --> Higher Priority
			if self.priority_func(self.elements[a_ctr]) <= self.priority_func(insertion_list[b_ctr]):
				new_list.append(self.elements[a_ctr])
				a_ctr += 1
			else:
				new_list.append(insertion_list[b_ctr])
				b_ctr += 1
		# Add remaining elements
		new_list.extend(self.elements[a_ctr:])
		new_list.extend(insertion_list[b_ctr:])
		# Change the list
		self.elements = copy(new_list)
		self.size += len(insertion_list)
	
	def dequeue(self):
		if self.size == 0:
			return None 
		else:
			self.size -= 1
			return self.elements.pop(0)

	def display(self):
		print(self.elements)


def count_natural_runs(state):
	cnt = 0
	broke = False
	prev = state[0]
	for i in range(1, len(state)):
		# Check if order changed
		if state[i] < prev:
			broke = True 
		# Store previous element
		prev = state[i]
		# If order changed, increment runs
		if broke:
			cnt += 1
			broke = False
	# Add 1 for the end of list
	cnt += 1 
	return cnt

def identity(n):
	return n

# TEST FOR NATURAL RUNS
print(count_natural_runs([1,2,3,6,7,4,5]))
print(count_natural_runs([1,4,6,2,5,3,7]))


if __name__ == '__main__':
	# Main Driver
	initial_state = list(map(int, input().split()))

