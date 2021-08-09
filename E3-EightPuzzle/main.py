import time

import BFS as BFS 
import Bidirectional_BFS as BiBFS
from StateFormulation import INITIAL_STATE, GOAL_STATE

line = "----------------------------"
runs = 2

print("\nINITIAL STATE")
for row in INITIAL_STATE:
	print(row)

print("\nGOAL STATE")
for row in INITIAL_STATE:
	print(row)


print("\n"+line)
print("Performing Biderictional BFS...")
total_time = 0
for i in range(runs):
	start_time = time.time()
	f_explored_states, r_explored_states, conn_state, f_parents, r_parents = BiBFS.search()
	total_time += time.time() - start_time
	# Display the output after the first run
	# The rest of the runs are used to average the runnning-time
	if i==0:
		print("\nSearch Complete. Path obtained is:\n")
		goal_path, f_depth, r_depth = BiBFS.deduce_path(conn_state, f_parents, r_parents)
		for state in goal_path:
			for row in state:
				print(row)
			print()
		print("\nCompleting {} runs of Bidrectional-BFS for run-time averaging...".format(runs))
BiBFS_time = total_time/runs
print("\nNo. of Distinct States Explored: ", len(f_explored_states.union(r_explored_states)))
print("Time Taken (avg. of 10 runs): {} seconds".format(runs, BiBFS_time))
print("Depth of Goal State: ", f_depth+r_depth+1)
print("Depth of Forward Search: ", f_depth)
print("Depth of Reverse Search: ", r_depth)


print("\n"+line)
print("Performing Traditional BFS...")
total_time = 0
for i in range(runs):
	start_time = time.time()
	explored_states, parents = BFS.search()
	total_time += time.time() - start_time
	# Display the output after the first run
	# The rest of the runs are used to average the runnning-time
	if i==0:
		print("\nSearch Complete. Path Obtained")
		goal_path = BFS.deduce_path(GOAL_STATE, parents)
		for state in goal_path:
			for row in state:
				print(row)
			print()
		print("\nCompleting {} runs of BFS for run-time averaging...".format(runs))
BFS_time = total_time/runs
print("\nTime Taken (avg. of 10 runs): {} seconds".format(runs, BFS_time))
print("No. of Distinct States Explored: ", len(explored_states))
print("Depth of Goal State: ", len(goal_path)-1)

print("\n"+line)
print("Time taken by traditional BFS: {} seconds".format(BFS_time))
print("Time taken by bidirectional BFS: {} seconds".format(BiBFS_time))