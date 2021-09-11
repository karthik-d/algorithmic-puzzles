from copy import copy
from StateFormulation import *
import numpy as np


def sample_population(population):
	num_draws = len(population)
	print("TEST:", population)
	# Create array with elements as per probability of choice
	population_fitness = [ count_non_attacks(state) 
							for state in population ]
	# Create a population sample
	population_sample = []
	for idx, state in enumerate(population):
		population_sample.extend([
			state for k in range(population_fitness[idx])
			])
	np.random.shuffle(population_sample)
	# Select parents and pair them up
	#print(population_sample)
	population_idx = [ x for x in range(len(population_sample)) ]
	parent_pairs_idx = np.random.choice(population_idx, num_draws)
	parent_pairs = [ population_sample[idx] for idx in parent_pairs_idx ]
	parent_pairs = [ (parent_pairs[i], parent_pairs[i+1])
						for i in range(num_draws//2) ]
	return parent_pairs
	

def crossover_pair(pair, population_size):
	crossover_idx = np.random.randint(1, population_size-1)
	result = []
	parent_1, parent_2 = pair
	result.append(parent_1[:crossover_idx+1] + parent_2[crossover_idx:])
	result.append(parent_2[:crossover_idx+1] + parent_1[crossover_idx:])
	return result
	

def mutate_state(state):
	mutation_idx = np.random.randint(0, len(state)+1)
	if mutation_idx == len(state):
		# No mutation
		pass
	else:
		mutated_state = np.random.randint(0, NUM_QUEENS)
		state[mutation_idx] = mutated_state
	return state


def search(population_size=8):
	population = [ generate_random_state() for k in range(population_size) ]

	while not any(map(is_goal_reached, population)):
		# Select parent-pairs from population as per probability of selection
		parent_pairs = sample_population(population)
		# Generate descendant population
		population_next = []
		for pair in parent_pairs:
			population_next.append(mutate_state(crossover_pair(pair, population_size)))
		population = copy(population_next)
	return population
		
			
