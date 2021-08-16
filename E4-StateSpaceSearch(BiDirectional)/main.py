import IterativeDeepening
import BidirectionalBFS
from StateFormulation import *


line = "----------------------------"


if __name__ == '__main__':

	num_expected_solns = 3
	print("\n"+line)
	print("ITERATIVE DEEPENING Search\n")
	goal_states, explored_states, parents, depths = IterativeDeepening.search(num_expected_solns)

	print("\nDISTINCT EXPLORED STATES COUNT: ", len(explored_states))

	print("\nGOAL STATES COUNT: ", len(goal_states))

	print("\nINITIAL STATE")
	print(INITIAL_STATE)

	print("\nGOAL STATES")
	for state in goal_states:
		print(state)

	print("\nEXPLORED STATES")
	for state in explored_states:
		print(state)

	for state in goal_states:
		print("\nPATH to reach", state)
		print("\n".join(IterativeDeepening.make_path_string(IterativeDeepening.deduce_path(state, parents), depths)))
		print(state, '--> GOAL STATE')

	# Bidirectional Search
	print("\n"+line)
	print("BIDIRECTIONAL Search\n")
	
	print("INITIAL STATE")
	print(INITIAL_STATE)
	results = BidirectionalBFS.search(GOAL_STATES)
	for goal_state in results:
		# Unpack result parameters
		f_explored_states, r_explored_states, conn_state, f_parents, r_parents = results[goal_state]
		print("\n"+line)
		print("For GOAL STATE", goal_state)
		
		explored_states = f_explored_states.union(r_explored_states)
		print("\nDISTINCT EXPLORED STATES COUNT: ", len(explored_states))
		print("\nEXPLORED STATES")
		for state in explored_states:
			print(state)
		
		print("\nPATH TAKEN")
		goal_path, f_depth, r_depth = BidirectionalBFS.deduce_path(conn_state, f_parents, r_parents)
		for state in goal_path:
			if(state==conn_state):
				print(state, '--> CONNECTING STATE')
			elif(state==goal_state):
				print(state, '--> GOAL STATE')
			else:
				print(state)

		

            