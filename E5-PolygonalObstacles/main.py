from StateFormulation import *

polygons = [
	Polygon([(1,1), (1,3), (4,3), (4,1)]),
	Polygon([(5,2), (6,4), (4,5)])
]

state_space = StateSpace(
	start = (0,0),
	end = (6,5),
	obstacles = polygons
)

"""
for edge in state_space.poly_edges:
	print(" - ".join(map(str, edge)))
print()
for state in state_space.states:
	print(state)
print()
"""

for point in state_space.get_next_states():
	print(point)

"""
# Intersection Test Cases
seg1 = ( Point([0,0]), Point([4,3]) )
seg2 = ( Point([1,1]), Point([4,1]) )
print(segments_intersect(seg1, seg2))
#
seg1 = ( Point([0,0]), Point([6,5]) )
seg2 = ( Point([1,3]), Point([4,3]) )
print(segments_intersect(seg1, seg2))
"""