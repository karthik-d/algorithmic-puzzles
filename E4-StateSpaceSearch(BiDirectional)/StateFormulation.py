# CONSTANTS

CAPACITY = (8,5,3)
NUM_JUGS = 3
INITIAL_STATE = (8,0,0)
GOAL_STATES = [(4,1,3), (4,4,0), (1,4,3)]

def get_next_states(state):

	# Transfer water from jug 'from_' to 'to'
    def transfer(from_, to):
        # Find bottleneck
        space = CAPACITY[to] - state[to]
        water = state[from_]
        transit = min(space, water)
        # Perform transfer
        new_state = list(state)
        new_state[to] += transit
        new_state[from_] -= transit
        return tuple(new_state)

    # From i to j
	# Check all possible combinations
    result = list()
    for i in range(NUM_JUGS):
        for j in range(NUM_JUGS):
            if (i==j):
				# Self-transfer is meaningless
                continue
            if CAPACITY[j]==state[j]:
                # Cannot fill more
				# Destination full
                continue
            if state[i]==0:
                # Nothing to transfer
				# Source empty
                continue
            result.append(transfer(i,j))
    
    return result

def is_goal_state(state):
    return 4 in state

# Compare the current state of `this` direction search
# to the fringe states of `that` direction search
def intersection_test(this_state, that_fringe):
	
	def are_states_same(state_A, state_B):
		for i in range(NUM_JUGS):
			if(state_A[i]!=state_B[i]):
				return False 
		return True
	
	for state in that_fringe:
		if are_states_same(state, this_state):
			return True
	return False