import time
from copy import deepcopy
from numpy import inf

from StateFormulation import *
from InstanceGenerator import generate_state_space
import BreadthFirstSearch as BFS 
import BestFirstSearch as Best_Greedy
import AStarSearch as AStar 


def run_with_timer(function, args):
	start = time.time()
	results = function(*args)
	return time.time()-start, results

def display_summary(results, exec_time):
	if results:
		print("Path Found")
	else:
		print("Path NOT Found")
	print("Time Taken: {time}s".format(time=exec_time))

line = '-'*50

# SIMPLE MANUAL TEST CASE (diagrams attached in 'Documentation')
print(line)
print("MANUAL TEST CASE")
print(line)

# Make Polygonal Obstacles
polygons = [
	Polygon([(220,616), (220,666), (251,670), (272,647)]),
	Polygon([(341,655), (359,667), (374,651), (366,577)]),
	Polygon([(311,530), (311,559), (339,578), (361,560), (361, 528), (336, 516)]),
	Polygon([(105,628), (151,670), (180,629), (156,577), (113, 587)]),
	Polygon([(118,517), (245,517), (245,577), (118,557)]),
	Polygon([(280,583), (333,583), (333,665), (280,665)]),
	Polygon([(252,594), (290,562), (264,538)]),
	Polygon([(198,635), (217,574), (182,574)]),
]
# Define State Space for Problem
state_space = StateSpace(
	start = (120,650),
	end = (380,560),
	obstacles = polygons
)

print(state_space)

print("\n\nBREADTH FIRST SEARCH")
print(line)
result = BFS.search(deepcopy(state_space))
if result:
	print("Path Found")
	print(result)
# Solution Found
# (120,650), (105,628), (118,517), (336,516), (361,528), (380,560)
# Cost: 421.3344534244741

print("\n\nBEST FIRST GREEDY SEARCH")
print(line)
result = Best_Greedy.search(deepcopy(state_space))
print(result)
if result:
	print("Path Found")
	print(result)
# Solution Found
# (120,650), (151,670), (251,670), (359,667), (374,651), (380,560)
# Cost: 358.0626920104638

print("\n\nA* SEARCH")
print(line)
result = AStar.search(deepcopy(state_space))
if result:
	print("Path Found")
	print(result)
# Solution Found
# (120,650), (151,670), (198,635), (220,616), (280,583), (339,578), (380,560)
# Cost: 297.02594348473116

input("\n\nPress any key to start Empirical Analysis...\n\n")

N_INSTANCES = 10
# Empirical Analysis using N_INSTANCES problems. Modify this constant as required
# Parameters analysed:
# 	Number of nodes generated 
#	Number of nodes expanded, 
#	Actual time taken, 
# 	Completeness, 
#	Optimality

print(line)
print("EMPIRICAL ANALYSIS")
print(line)

# Overall Times
bfs_time = 0
bestfs_time = 0
astar_time = 0
# Overall Completions
bfs_completes = 0
bestfs_completes = 0
astar_completes = 0
# Overall Optimal Solution
bfs_optimal = 0
bestfs_optimal = 0
astar_optimal = 0
# Generate and Run instances
for i in range(N_INSTANCES):
	state_space = generate_state_space()
	# Run BFS
	bfs_exec_time, bfs_results = run_with_timer(
		function=BFS.search, 
		args=(deepcopy(state_space),)
	)	
	# Run Best-First
	bestfs_exec_time, bestfs_results = run_with_timer(
		function=Best_Greedy.search, 
		args=(deepcopy(state_space),)
	)	
	# Run A*	
	astar_exec_time, astar_results = run_with_timer(
		function=AStar.search, 
		args=(deepcopy(state_space),)
	)	
	# Collect Summaries
	# Running time
	bfs_time += bfs_exec_time
	bestfs_time += bestfs_exec_time
	astar_time += astar_exec_time
	# Completion
	if bfs_results:
		bfs_completes += 1
		bfs_cost = bfs_results[0].cost
	else:
		bfs_cost = inf
	if bestfs_results:
		bestfs_completes += 1
		bestfs_cost = bestfs_results[0].cost
	else:
		bestfs_cost = inf
	if astar_results:
		astar_completes += 1
		astar_cost = astar_results[0].cost
	else:
		astar_cost = inf
	# Optimality
	opt_cost = min([bfs_cost, bestfs_cost, astar_cost])
	if bfs_cost == opt_cost:
		bfs_optimal += 1
	if bestfs_cost == opt_cost:
		bestfs_optimal += 1
	if astar_cost == opt_cost:
		astar_optimal += 1

	# Display Instance-Wise Summary
	print("INSTANCE", i+1)
	print(line)
	print(state_space)
	# For BFS
	print("\nBREADTH FIRST SEARCH")
	print(line)
	display_summary(bfs_exec_time, bfs_results)
	# For Best First
	print("\nBEST FIRST GREEDY SEARCH")
	print(line)
	display_summary(bestfs_exec_time, bestfs_results)
	# For A*
	print("\nA* SEARCH")
	print(line)
	display_summary(astar_exec_time, astar_exec_time)
	print("\n\n")



