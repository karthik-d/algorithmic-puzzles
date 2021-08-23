from numpy import inf

class Point:
	
	def __init__(self, coords):
		self.x = coords[0]
		self.y = coords[1]

	def slope(self, other_pt):
		horizontal = self.x - other_pt.x
		vertical = self.y - other_pt.y
		if horizontal==0:
			# Attach correct sign to infinity
			return inf*vertical
		else:
			return vertical/horizontal

	def __eq__(self, other_pt):
		return self.x == other_pt.x and self.y==other_pt.y

	def __str__(self):
		return '({x},{y})'.format(x=self.x, y=self.y)


class Polygon:

	def __init__(self, vertices):
		self.vertices = [ Point(vertex) for vertex in vertices ]
		self.edges = self.find_edges()
		
	def find_edges(self):
		# Polygon Edge is an ordered set (tuple) of two adjacent points
		edges = []
		for i in range(len(self.vertices)-1):
			edges.append((self.vertices[i], self.vertices[i+1]))
		edges.append((self.vertices[-1], self.vertices[0]))
		return edges


def segments_intersect(seg_1, seg_2):
	# Check if seg_1 intersects/touches seg_2
	# If the orientation of seg_1 wrt either ends of seg_2 are different (or one is collinear), they intersect/touch
	orient12_1 = get_orientation((seg_1[0], seg_1[1], seg_2[0]))
	orient12_2 = get_orientation((seg_1[0], seg_1[1], seg_2[1]))
	# (not any([orient12_1, orient12_2])) ==> Check if one of them is 0
	if orient12_1==orient12_2:
		return False
	# Check if seg_2 intersects/touches seg_1
	orient21_1 = get_orientation((seg_2[0], seg_2[1], seg_1[0]))
	orient21_2 = get_orientation((seg_2[0], seg_2[1], seg_1[1]))
	if orient21_1==orient21_2:
		return False
	return True


def get_orientation(three_pt_sequence):
	# Returns the orientation of a sequence of three points
	# 0: Collinear, -1: Clockwise, +1: Anti-Clockwise
	pt1, pt2, pt3 = three_pt_sequence
	slope_1 = pt1.slope(pt2)
	slope_2 = pt2.slope(pt3)
	print(slope_1, slope_2)
	# Evaluate slope change
	change = slope_1 - slope_2
	if change<0:
		return -1
	if change>0:
		return 1
	return 0


class StateSpace:

	def __init__(self, start, end, obstacles):
		# State Space Constants
		self.start = Point(start)
		self.end = Point(end)
		self.obstacles = obstacles
		self.poly_edges = self.get_poly_edges()
		self.states = [self.start, self.end] + self.get_poly_vertices()
		# Current State Representation
		self.curr_state = self.start 
		self.curr_polygon = None  
		# Store the polygon of current state 

	def get_poly_vertices(self):
		# Poly_Edges is the set of all edges of the obstacles in the state space
		vertices = []
		for polygon in self.obstacles:
			vertices.extend(polygon.vertices)
		return vertices

	def get_poly_edges(self):
		# Poly_Edges is the set of all edges of the obstacles in the state space
		edges = []
		for polygon in self.obstacles:
			edges.extend(polygon.edges)
		return edges

	def is_reachable(self, destn, src):
		# Already checked that destn and src are not in the same polygon
		# Check if the path from src to destn intersects any other edge
		path = (src, destn)
		for edge in self.poly_edges:
			#print(" - ".join(map(str, edge)))
			print(" - ".join(map(str, path)))
			print(" - ".join(map(str, edge)))
			print(segments_intersect(edge, path))
			print()
			if segments_intersect(edge, path):
				return False
		return True

	def get_next_states(self, visited=[]):
		# Excludes visited states
		# Either: 1. Adjacent vertex in same polygon
		#     Or: 2. Non-obstructing path to vertex of other polygon
		next_states = []
		for state in self.states:
			if state == self.curr_state:
				continue 
			if state in visited:
				continue 
			if self.curr_polygon and (state in self.curr_polygon.vertices):
				# Allow if it is an adjacent vertex
				num_vertices = len(self.curr_polygon.vertices)
				for i in range(num_vertices):
					if self.curr_polygon.vertices[i] == self.curr_state:
						# Check if state is previous or next vertex
						if state in ( self.curr_polygon.vertices[(i+1)%num_vertices], self.curr_polygon.vertices[i-1] ):
							next_states.append(state)
							continue
			if self.is_reachable(state, self.curr_state):
				next_states.append(state)
		return next_states


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
"""