from Queue import Queue 
from StateFormulation import *


def deduce_path(connecting_state, f_parents, r_parents):

	def deduce_path_rec(f_state, r_state, path_seq, f_depth, r_depth):
		f_parent = f_parents[f_state] if f_state is not None else None
		r_parent = r_parents[r_state] if r_state is not None else None
		recurse = False
		
		if f_parent is not None:
			path_seq = [f_parent] + path_seq
			f_depth += 1
			recurse = True
		if r_parent is not None:
			path_seq = path_seq + [r_parent]
			r_depth += 1
			recurse = True 
		
		if recurse:
			return deduce_path_rec(f_parent, r_parent, path_seq, f_depth, r_depth)
		else:
			return path_seq, f_depth, r_depth

	return deduce_path_rec(connecting_state, connecting_state, [connecting_state], 0, 0)


def search(goal_states):

	def search_chosen_goal(goal_state):

		f_state_space = Queue([INITIAL_STATE])
		f_explored_states = set()
		f_parents = {INITIAL_STATE: None}

		r_state_space = Queue([goal_state])
		r_explored_states = set()
		r_parents = {goal_state: None}

		while(not f_state_space.is_empty() or not r_state_space.is_empty()):
			# Forward Search
			f_state = f_state_space.dequeue()
			if f_state not in f_explored_states:
				# Explore now
				f_explored_states.add(f_state)
				if intersection_test(f_state, r_state_space.get_contents()):
					return f_explored_states, r_explored_states, f_state, f_parents, r_parents 
				fringe = get_next_states(f_state)
				f_state_space.enqueue(fringe)
				for new_state in fringe:
					if new_state not in f_parents:
						f_parents[new_state] = f_state

			# Reverse Search
			r_state = r_state_space.dequeue()
			if r_state not in r_explored_states:
				# Explore now
				r_explored_states.add(r_state)
				if intersection_test(r_state, f_state_space.get_contents()):
					return f_explored_states, r_explored_states, r_state, f_parents, r_parents
				fringe = get_next_states(r_state)
				r_state_space.enqueue(fringe)
				for new_state in fringe:
					if new_state not in r_parents:
						r_parents[new_state] = r_state
		
		return False 

	results = dict()
	for goal in goal_states:
		result = search_chosen_goal(goal)
		if not result:
			continue
		results[goal] = result 
	return results
		