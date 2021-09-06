# A random-restart version of the Hill-Climbing search algorithm
# No sideways moves are allowed. If plateau is reacheed, restart is applied

from StateFormulation import *

def search():
	restarts = 0
	while True:
		state = generate_random_state()
		# Reset at each restart
		transitions = [ state ]
		while True:
			curr_attacks = count_attacks(state)
			if curr_attacks == 0:
				# Goal reached
				return state, transitions, restarts
			# Generate next best state
			move, next_attacks = get_next_best_move(state)
			if next_attacks >= curr_attacks:
				# At some local maxima or plateau
				# Restart search
				restarts += 1
				break
			# Move to the best successor state
			in_col, to_row = move
			state[in_col] = to_row 
			# Add this new state to set of transitions
			transitions.append(state)
		# Restart search with new random start
		state = generate_random_state()
	
