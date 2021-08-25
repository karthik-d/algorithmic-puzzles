import time
from copy import deepcopy

from StateFormulation import *
from InstanceGeneratore import *
import BreadthFirstSearch as BFS 
import BestFirstSearch as Best_Greedy
import AStarSearch as AStar 

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


N_INSTANCES = 100
# Empirical Analysis using N_INSTANCES problems. Modify this constant as required
print(line)
print("EMPIRICAL ANALYSIS")
print(line)
