from IterativeDeepening import *
from StateFormulation import *


line = "----------------------------"


if __name__ == '__main__':

	num_expected_solns = 3
	print("\n"+line)
	print("ITERATIVE DEEPENING Search\n")
	goal_states, explored_states, parents, depths = IterativeDeepening(num_expected_solns)

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
		print("\n".join(make_path_string(deduce_path(state, parents), depths)))
		print(state, '--> GOAL STATE')
		

            