from HillClimbing import search as HC_search
from StateFormulation import display_state

goal, transitions, restarts = HC_search()

print("INITIAL State: ", transitions[0])
print()
display_state(transitions[0])
for state in transitions[1:-1]:
	print("\t\t|\n\t\t|\n\t\tV\n")
	print("State:", state)
	print()
	display_state(state)
print("\t\t|\n\t\t|\n\t\tV\n")
print("\nGOAL State:", transitions[-1])
display_state(goal)

print("\nNumber of Restarts:", restarts)