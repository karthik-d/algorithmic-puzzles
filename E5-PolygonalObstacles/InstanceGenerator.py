import numpy.random as random

from StateFormulation import *
from geometry import *

# CONSTANTS (modify as required)
MIN_OBSTACLES = 10
MAX_OBSTACLES = 20
MIN_VERTICES_POLY = 3
MAX_VERTICES_POLY = 10
MIN_COORDINATE_VALUE = -200
MAX_COORDINATE_VALUE = +200


def generate_coordinates():
	# Return a random 2D point within the coordinate limits
	return (random.randint(MIN_COORDINATE_VALUE, MAX_COORDINATE_VALUE+1), 
			random.randint(MIN_COORDINATE_VALUE, MAX_COORDINATE_VALUE+1))


def generate_polygon():
	# Randomly determine number of vertices and generate points
	num_vertices = random.randint(MIN_COORDINATE_VALUE, MAX_OBSTACLES+1)
	vertices = [ generate_coordinates() for k in range(num_vertices) ]
	return Polygon(vertices)


def generate_state_space():
	# Randomly determine number of obstacles and generate polygons
	num_obstacles = random.randint(MIN_OBSTACLES, MAX_OBSTACLES+1)
	polygons = []
	for i in range(num_obstacles):
		polygons.append(generate_polygon())
	# Make State-Space
	state_space = StateSpace(
		start=generate_coordinates(),
		end=generate_coordinates(),
		obstacles=polygons
	)
	return state_space
	