from geometry import *

class StateSpace:

	def __init__(self, start, end, obstacles):
		# State Space Constants
		self.start = Point(start)
		self.end = Point(end)
		self.obstacles = obstacles
		self.poly_edges = self.get_poly_edges()
		self.states = [self.start, self.end] + self.get_poly_vertices()
		self.visited = set()
		# Current State Representation
		self.curr_state = None
		self.curr_polygon = None
		# Store the polygon of current state 

	def move_to_state(self, new_state):
		prev_state = self.curr_state
		self.curr_state = new_state
		self.curr_polygon = self.get_curr_polygon()
		if prev_state is not None:
			self.visited.add(prev_state)

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

	def at_goal_state(self):
		return self.curr_state == self.end

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

	def __str__(self):
		display_string = "Start: {start}\nGoal: {goal}\nPolygons:\n{polygon}".format(
			start=self.start, 
			goal=self.end, 
			polygon='\n'.join(map(str, self.obstacles))
		)
		return display_string