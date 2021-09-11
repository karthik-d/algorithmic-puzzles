from GeneticAlgorithm import search as GA_search
from StateFormulation import display_state

population_size = 8
print("Running Genetic Algorithm...")
goal_state, num_generations = GA_search(population_size=population_size)
print("\nGOAL STATE REACHED:", goal_state)
print()
display_state(goal_state)
print("\nPopulation Size:", population_size)
print("Number of Generations:", num_generations)