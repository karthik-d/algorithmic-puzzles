from Queue import *

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

def BFS():
    explored_states = list()
    all_paths = Queue([INITIAL_STATE])
    goal_paths = list()
    goal_states = list()
    state_space = Queue([INITIAL_STATE])
    while not state_space.is_empty():
        state = state_space.dequeue()
        path = all_paths.dequeue()
        if state in explored_states:
            continue
        explored_states.append(state)
        if goal_test(state):
            goal_states.append(state)
            goal_paths.append(path)
        fringe = next_states(state)
        state_space.enqueue(fringe)
        for n_state in fringe:
            new_path = list(path)
            new_path.append(n_state)
            all_paths.enqueue([new_path])
    return goal_states, goal_paths, explored_states

goal_state, goal_paths, explored_states = BFS()
print("\nDISTINCT STATES COUNT:", len(explored_states))
print("\nGOAL STATES:", goal_state)
print("\nEXPLORED STATES:", explored_states)
ctr = 1
for path in goal_paths:
    print("\nPATH", ctr)
    print(INITIAL_STATE)
    for vertex in path[3:]:
        print(vertex)
    ctr += 1

            