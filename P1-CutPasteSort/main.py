from copy import copy, deepcopy

def identity(n):
	return n


class PriorityQueue:

	def __init__(self, priority_func):
		self.elements = []
		self.size = 0
		self.priority_func = priority_func
	
	def enqueue(self, insertion_list):
		insertion_list.sort(key=self.priority_func)
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
		if self.is_empty():
			return None
		else:
			self.size -= 1
			return self.elements.pop(0)

	def is_empty(self):
		return self.size == 0

	def display(self):
		print(self.elements)

"""
# TEST FOR PRIORITY QUEUE
queue = PriorityQueue(identity)
queue.enqueue([1,5,6,3])
queue.enqueue([4,7,9])
queue.display()
"""

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

"""
# TEST FOR NATURAL RUNS
print(count_natural_runs([1,2,3,6,7,4,5]))
print(count_natural_runs([1,4,6,2,5,3,7]))
"""

def positional_distance(state):
	distance = 0
	for i in range(len(state)):
		distance += abs((state[i]-1)-i)
	return distance

def count_incorrect_posns(state):
	cnt = len(state)
	for i in range(len(state)):
		if i == state[i]-1:
			cnt -= 1
	return cnt 

"""
print(count_incorrect_posns([1,5,4,3,2]))
print(count_incorrect_posns([3,2,5,4,1]))
"""

def count_inversions(state):
	cnt = 0
	for i in range(len(state)-1):
		for j in range(i+1, len(state)):
			if state[i]>state[j]:
				cnt += 1
	return cnt

def count_non_consecutive(state):
	prev = state[0]
	cnt = 0 if prev==1 else 1
	for n in state[1:]:
		if prev+1 != n:
			cnt += 1
		prev = n
	return cnt
		

# STATE SPACE

def get_next_states(state):
	next_states = []
	length = len(state)
	# Generate cut points
	for cut_start in range(length+1):
		for cut_end in range(cut_start+1, length+1):
			temp_state = deepcopy(state)
			cut_portion = temp_state[cut_start:cut_end]
			cut_remain = temp_state[:cut_start] + temp_state[cut_end:]
			# Generate insert points
			for insert_pt in range(len(cut_remain)+1):
				new_state = cut_remain[:insert_pt] + cut_portion[:] + cut_remain[insert_pt:]
				if new_state != state:
					next_states.append(new_state)
	return next_states
			
"""
# TEST FOR NEXT-STATES
inputs = [
	[1, 2, 3],
	#[1, 2, 3, 4],
]
for in_ in inputs:
	next_states = get_next_states(in_)
	print(next_states, len(next_states))
"""
"""
q = PriorityQueue(count_incorrect_posns) 
q.enqueue(get_next_states([5,4,3,2,1]))
q.display()
"""

def goal_test(state):
	prev = state[0]
	for i in state[1:]:
		if i < prev:
			return False 
		prev = i
	return True 

"""
# TEST FOR GOAL TEST
inputs = [
	[1,2,3,4],
	[1,3,2,4],
	[1,4,3,2]
]
for in_ in inputs:
	print(goal_test(in_))
"""

def best_first_search(initial_state):
	# Least natural_runs --> First Priority
	# state_space = PriorityQueue(count_natural_runs) 
	# state_space = PriorityQueue(positional_distance) 
	# state_space = PriorityQueue(count_incorrect_posns) 
	state_space = PriorityQueue(count_non_consecutive) 
	state_space.enqueue([initial_state])
	# Track parents
	parents = {
		tuple(initial_state): None
	}
	# Run search
	while not state_space.is_empty():
		curr_state = state_space.dequeue()
		if goal_test(curr_state):
			print("Found")
			return curr_state, parents
		fringe = get_next_states(curr_state)
		state_space.enqueue(fringe)
		# Record parents
		for state in fringe:
			state_key = tuple(state)
			if state_key in parents:
				pass 
			else:
				parents[state_key] = tuple(curr_state)
	return None, None

def get_path(state, parents):
	state = tuple(state)
	path = [ state ]
	while True:
		parent = parents[state]
		if parent is None:
			break
		path.append(parent)
		state = parent
	return path[::-1]
			


if __name__ == '__main__':
	# Main Driver
	initial_state = list(map(int, input().split()))
	goal_state, parents = best_first_search(initial_state)
	for state in get_path(goal_state, parents):
		print(state)


