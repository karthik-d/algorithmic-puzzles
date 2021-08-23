class Point:
	
	def __init__(self, point):
		self.x = point[0]
		self.y = point[1]


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


class StateSpace:

	def __init__(self, start, end, obstacles):
		self.start = Point(start)
		self.end = Point(end)
		self.obstacles = [ Polygon(polygon) for polygon in obstacles ]
		self.states = [self.start + self.end].extend(self.get_poly_points())
		self.poly_edges = self.find_poly_edges

	def get_poly_edges(self):
		# Poly_Edges is the set of all edges of the obstacles in the state space
		edges = []
		for polygon in self.obstacles:
			edges.extend(polygon.edges)
		return edges

	def get_poly_points(self):
		points = []
		for polygon in self.obstacles:
			points.extend(polygon.vertices)
		return points

	def is_reachable(self, destn, src):
		

	def get_next_states(self, curr_state, visited=[]):
		# Excludes visited states
		next_states = []
		for state in self.states:
			if state == curr_state:
				continue 
			if state in visted:
				continue 
			if not is_reachable(state, curr_state):
				continue 
			next_states.append(state)
		return next_states

