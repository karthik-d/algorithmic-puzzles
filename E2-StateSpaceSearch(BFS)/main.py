from Queue import *
from StateFunctions import *

line = "----------------------------"

def BFS():

    all_paths = Queue([[INITIAL_STATE]])
    state_space = Queue([INITIAL_STATE])
    goal_paths = list()
    goal_states = list()
    explored_states = list()

    while not state_space.is_empty():
		# Get next state and its path
        state = state_space.dequeue()
        path = all_paths.dequeue()
		# Skip iteration if state already explored
        if state in explored_states:
            continue
        explored_states.append(state)
		# Check if state is a goal-state
        if is_goal_state(state):
            goal_states.append(state)
            goal_paths.append(path)
		# Find the next states
        fringe = get_next_states(state)
        state_space.enqueue(fringe)
		# Add path to each fringe state
        for n_state in fringe:
            new_path = list(path[:])
            new_path.append(n_state)
            all_paths.enqueue([new_path])

    return goal_states, goal_paths, explored_states

if __name__ == '__main__':
	goal_states, goal_paths, explored_states = BFS()
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
	for i in range(len(goal_paths)):
		print("\nPATH", i+1)
		print("To reach", goal_paths[i][-1])
		print(line)
		for vertex in goal_paths[i][:-1]:
			print(vertex)
		print(goal_paths[i][-1], '--> GOAL STATE')
		print(line)

            