from numpy import inf
from math import pi, atan, degrees

class Point:
	
	def __init__(self, coords):
		self.x = coords[0]
		self.y = coords[1]

	def __eq__(self, other_pt):
		return self.x == other_pt.x and self.y==other_pt.y

	def __str__(self):
		return '({x},{y})'.format(x=self.x, y=self.y)

	def __hash__(self):
		# Represent Point as a 'tuple' and use tuple's hash function
		return hash((self.x, self.y))


class Vector:
	
	def __init__(self, src, destn):
		# src and destn are Point instances
		self.x = destn.x - src.x
		self.y = destn.y - src.y
		self.quadrant = self.get_quadrant()
		self.direction = self.get_direction()

	def get_direction(self):
		# By defn, theta of vector wrt x-axis
		# Set offset as per quadrant
		offset = pi if self.quadrant in (2,3) else 0
		if self.x==0:
			# Attach sign of y to infinity
			tan_theta = inf*(self.y) 
		else:
			tan_theta = atan(self.y/self.x) 
		direction = offset + atan(tan_theta)
		return Vector.normalize_angle(direction)

	def get_quadrant(self):
		if self.x>=0:
			if self.y>=0:
				return 1
			else:
				return 4
		else:
			if self.y>=0:
				return 2
			else:
				return 3

	def get_relative_direction(self, other_vector):
		return Vector.normalize_angle(self.direction - other_vector.direction)

	def is_zero_vector(self):
		return self.x == 0 and self.y==0

	@staticmethod
	def normalize_angle(angle):
		# Return angle in rannge [0,360]
		while angle<0:
			angle += 2*pi 
		return angle


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


def has_duplicates(points):
	return len(set(points))!=len(points)


def segments_intersect(seg_1, seg_2):
	# If any of the points are repeated, they touch => No obstruction
	if has_duplicates(seg_1+seg_2):
		return False
	# Check if seg_1 intersects/touches seg_2
	# If the orientation of seg_1 wrt either ends of seg_2 are different (or one is collinear), they intersect
	orient12_1 = get_orientation((seg_1[0], seg_1[1], seg_2[0]))
	orient12_2 = get_orientation((seg_1[0], seg_1[1], seg_2[1]))
	# (not any([orient12_1, orient12_2])) ==> Check if one of them is 0
	if (not any([orient12_1, orient12_2])) or orient12_1==orient12_2:
		return False
	# Check if seg_2 intersects/touches seg_1
	orient21_1 = get_orientation((seg_2[0], seg_2[1], seg_1[0]))
	orient21_2 = get_orientation((seg_2[0], seg_2[1], seg_1[1]))
	if (not any([orient21_1, orient21_2])) or orient21_1==orient21_2:
		return False
	return True


def get_orientation(three_pt_sequence):
	# Returns the orientation of a sequence of three points
	# 0: Collinear, -1: Clockwise, +1: Anti-Clockwise
	pt1, pt2, pt3 = three_pt_sequence
	vector_1 = Vector(pt1, pt2)
	vector_2 = Vector(pt2, pt3)
	# Check if adjacent points are same - Direction can't be found
	if vector_1.is_zero_vector() or vector_2.is_zero_vector():
		return 0
	# Find angle between vectors
	relative_direction =  vector_2.get_relative_direction(vector_1)
	# Determine orientation
	if relative_direction < pi:
		return -1
	elif relative_direction > pi:
		return 1
	else:
		return 0


class StateSpace:

	def __init__(self, start, end, obstacles):
		# State Space Constants
		self.start = Point(start)
		self.end = Point(end)
		self.obstacles = obstacles
		self.poly_edges = self.get_poly_edges()
		self.states = [self.start, self.end] + self.get_poly_vertices()
		self.visited = []
		# Current State Representation
		self.curr_state = None
		self.curr_polygon = None
		# Store the polygon of current state 

	def move_to_state(self, new_state):
		prev_state = self.curr_state
		self.curr_state = new_state
		self.curr_polygon = self.get_curr_polygon()
		if prev_state is not None:
			self.visited.append(prev_state)

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

	def get_curr_polygon(self):
		# Check if move was on same polygon
		if self.curr_polygon and self.curr_state in self.curr_polygon.vertices:
			return self.curr_polygon
		# Find polygon 
		for polygon in self.obstacles:
			if self.curr_state in polygon.vertices:
				return polygon 
		# Set to None for terminal points
		return None

	def is_goal_state(self, state):
		return state == self.end

	def is_visited(self, state):
		return state in self.visited

	def is_reachable(self, destn, src):
		# Already checked that destn and src are not in the same polygon
		# Check if the path from src to destn intersects any other edge
		path = (src, destn)
		for edge in self.poly_edges:
			if segments_intersect(edge, path):
				return False
		return True

	def get_next_states(self, include_visited=False):
		# Excludes visited states
		# Either: 1. Adjacent vertex in same polygon
		#     Or: 2. Non-obstructing path to vertex of other polygon
		next_states = []
		for state in self.states:
			# Check if state is same as current
			if state == self.curr_state:
				continue 
			# Skip if state is visited
			if not include_visited and self.is_visited(state):
				continue 
			# Case: State is part of same polygon (grazing allowed)
			if self.curr_polygon and (state in self.curr_polygon.vertices):
				# Allow if it is an adjacent vertex
				num_vertices = len(self.curr_polygon.vertices)
				for i in range(num_vertices):
					if self.curr_polygon.vertices[i] == self.curr_state:
						# Check if state is previous or next vertex
						if state in ( self.curr_polygon.vertices[(i+1)%num_vertices], self.curr_polygon.vertices[i-1] ):
							next_states.append(state)
				continue
			# Case: State is not part of same polygon
			if self.is_reachable(state, self.curr_state):
				next_states.append(state)
		return next_states