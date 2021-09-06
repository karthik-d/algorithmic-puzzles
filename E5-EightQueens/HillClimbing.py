# A random-restart version of the Hill-Climbing search algorithm
# No sideways moves are allowed. If plateau is reacheed, restart is applied

from StateFormulation import *

def search():
	state = generate_random_state()
	
