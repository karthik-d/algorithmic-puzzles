from numpy import inf

class Point:
	
	def __init__(self, point):
		self.x = point[0]
		self.y = point[1]

	def slope(self, other_pt):
		horizontal = self.x - other_pt.x
		if horizontal==0:
			return inf
		vertical = self.y - other_pt.y
		return vertical/horizontal

	def __eq__(self, other_pt):
		return self.x == other_pt.x and self.y==other_pt.y


class Polygon:

	def __init__(self, vertices):
		self.vertices = [ Point(vertex) for vertex in vertices ]
		self.edges = self.find_edges()
		
	def find_edges(self):
		# Polygon Edge is an ordered set (tuple) of two adjacent points
		edges = []
		for i in range(len(self.vertices)-1):
			edges.append((self.vertices[i], self.vertices[i+1]))
		edges.append((self.vertices[0], self.vertices[-1]))
		return edges


def segments_intersect(seg_1, seg_2):
	# Check if seg_1 intersects/touches seg_2
	# If the orientation of seg_1 wrt either ends of seg_2 are different, they intersect/touch
	if get_orientation(seg_1[0], seg_1[1], seg_2[0]) == get_orientation(seg_1[0], seg_1[1], seg_2[1]):
		return False
	# Check if seg_2 intersects/touches seg_1
	if get_orientation(seg_2[0], seg_2[1], seg_1[0]) == get_orientation(seg_2[0], seg_2[1], seg_1[1]):
		return False
	return True


def get_orientation(thee_pt_sequence):
	# Returns the orientation of a sequence of three points
	# 0: Collinear, -1: Clockwise, +1: Anti-Clockwise
	pt1, pt2, pt3 = three_pt_sequence
	slope_1 = pt1.slope(pt2)
	slope_2 = pt2.slope(pt3)
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
		self.obstacles = [ Polygon(polygon) for polygon in obstacles ]
		self.poly_edges = self.find_poly_edges
		# Current State Representation
		self.curr_state = self.start 
		self.curr_polygon = None  
		# Store the polygon of current state 

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
			if state in visted:
				continue 
			if state in self.curr_polygon.vertices:
				# Allow if it is an adjacent vertex
				num_vertices = len(self.curr_polygon.vertices)
				for i in range(num_vertices):
					if self.curr_polygon.vertices[i] == self.curr_state:
						# Check if state is previous or next vertex
						if state in ( self.curr_polygon.vertices[(i+1)%num_vertices], self.curr_polygon.vertices[i-1] ):
							next_states.append(state)
							continue
			if is_reachable(state, curr_state):
				next_states.append(state)
		return next_states

