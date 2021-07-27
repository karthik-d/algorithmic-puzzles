# CONSTANTS

CAPACITY = (8,5,3)
NUM_JUGS = 3
INITIAL_STATE = (8,0,0)

def next_states(state):

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
    result = list()
    for i in range(NUM_JUGS):
        for j in range(NUM_JUGS):
            if (i==j):
                continue
            if CAPACITY[j]==state[j]:
                # Cannot fill more
                continue
            if state[i]==0:
                # Nothing to transfer
                continue
            result.append(transfer(i,j))
    
    return result

def goal_test(state):
    return 4 in state