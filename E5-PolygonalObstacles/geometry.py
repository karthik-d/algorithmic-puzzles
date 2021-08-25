from numpy import inf
from math import pi, atan, degrees

class Point:
	
	def __init__(self, coords):
		self.x = coords[0]
		self.y = coords[1]

	def distance_to(self, other_pt):
		horizontal_sq = (self.x-other_pt.x)**2
		vertical_sq = (self.y-other_pt.y)**2
		return (horizontal_sq+vertical_sq)**0.5

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

	def __str__(self):
		display_string = '{sides}-sided Polygon : {vertices}'.format(
			sides=len(self.vertices),
			vertices='{'+', '.join(map(str, self.vertices))+'}'
		)
		return display_string
		


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