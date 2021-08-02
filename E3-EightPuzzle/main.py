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
	conn_state, f_parents, r_parents = BiBFS.search()
	total_time += time.time() - start_time
	# Display the output after the first run
	# The rest of the runs are used to average the runnning-time
	if i==0:
		print("\nSearch Complete. Path obtained is:\n")
		for state in BiBFS.deduce_path(conn_state, f_parents, r_parents):
			for row in state:
				print(row)
			print()
		print("\nCompleting {} runs of Bidrectional-BFS for run-time averaging...".format(runs))
BiBFS_time = total_time/runs
print("\nTime Taken (avg. of {} runs): {} seconds".format(runs, BiBFS_time))


print("\n"+line)
print("Performing Traditional BFS...")
total_time = 0
for i in range(runs):
	start_time = time.time()
	parents = BFS.search()
	total_time += time.time() - start_time
	# Display the output after the first run
	# The rest of the runs are used to average the runnning-time
	if i==0:
		print("\nSearch Complete. Path Obtained")
		for state in BFS.deduce_path(GOAL_STATE, parents):
			for row in state:
				print(row)
			print()
		print("\nCompleting {} runs of BFS for run-time averaging...".format(runs))
BFS_time = total_time/runs
print("\nTime Taken (avg. of {} runs): {} seconds".format(runs, BFS_time))


print("\n"+line)
print("Time taken by traditional BFS: {} seconds".format(BFS_time))
print("Time taken by bidirectional BFS: {} seconds".format(BiBFS_time))

