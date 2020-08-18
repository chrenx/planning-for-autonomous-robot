import operator
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fitness import Fitness

POPULATION_SIZE = 10
ELITE_SIZE = 5
MUTATION_RATE = 0.01
drawing = []
min_route = []  # [[best route], total cost]


def ga_tsp(city_list, city_map, generations):
    """
    :param generations: generation number
    :param city_map: completed graph implemented with adjacency matrix
    :param city_list: list of all the cities represented by number in sequence
    """
    global min_route
    pop = initial_population(city_list)
    ranked = rank_routes_by_fitness(pop, city_map)
    # progress.append(1 / ranked[0][1])
    # print(pop)
    # print("\n")
    # print(ranked)
    print("Initial distance: " + str(1 / ranked[0][1]))
    min_route.append(pop[ranked[0][0]])
    min_route.append(1 / ranked[0][1])
    for i in range(generations):
        pop = next_generation(pop, city_map)
        ranked = rank_routes_by_fitness(pop, city_map)
        if 1 / ranked[0][1] < min_route[1]:
            min_route[0] = pop[ranked[0][0]]
            min_route[1] = 1 / ranked[0][1]
    print("Best distance: " + str(min_route[1]))
    print("Best route: " + str(min_route[0]))
    """
    ranked = rank_routes_by_fitness(pop, city_map)
    print("Final distance: " + str(1 / ranked[0][1]))
    best_route_index = rank_routes_by_fitness(pop, city_map)[0][0]
    best_route = pop[best_route_index]
    print("Final route: " + str(best_route))
    """
    plt.plot(drawing)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.savefig('ga_tsp.png')
    return min_route[0]  # best_route


def next_generation(current_generation, city_map):
    """
    :param current_generation: current all routes
    :param city_map: completed graph implemented with adjacency matrix
    :return: next generation of routes
    """
    global drawing
    pop_ranked = rank_routes_by_fitness(current_generation, city_map)
    drawing.append(1 / pop_ranked[0][1])
    selected = selection(pop_ranked)
    mating_pool = mating(current_generation, selected)
    children = breed_population(mating_pool)
    next_gene = mutate_population(children)
    return next_gene


def initial_population(city_list):
    """
    :param city_list: list of all the cities represented by number in sequence
    :return: population pool
    """
    population = []
    for i in range(POPULATION_SIZE):
        population.append(random.sample(city_list, len(city_list)))
    return population  # no duplicates


def rank_routes_by_fitness(population, city_map):
    """
    :param population: population pool
    :param city_map: completed graph implemented with adjacency matrix
    :return: sorted routes by fitness score in descending order
    Return example: [(2, 0.5), (0, 0.3), (1, 0.1)], whose first element is
    the index of the route in population list.
    """
    results = {}
    for i in range(len(population)):
        # e.g. {2: 0.7, 0: 0.5, 1: 0.3}
        results[i] = Fitness(population[i], city_map).get_fitness()
    return sorted(results.items(), key=operator.itemgetter(1), reverse=True)


def selection(pop_ranked):
    """
    :param pop_ranked: output from rank_routes_by_fitness
    :return: the index of chosen routes
    """
    selection_result = []
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index", "Fitness Score"])
    total_score = df["Fitness Score"].sum()
    df['percent'] = 100 * df["Fitness Score"] / total_score
    for i in range(ELITE_SIZE):
        selection_result.append(pop_ranked[i][0])

    while len(selection_result) <= POPULATION_SIZE:
        temp = random.random() * 100
        for i in range(len(pop_ranked)):
            if temp <= df.iat[i, 2]:
                selection_result.append(pop_ranked[i][0])
    """
    for i in range(len(pop_ranked) - ELITE_SIZE):
        temp = random.random() * 100
        for j in range(len(pop_ranked)):
            if temp <= df.iat[i, 2]:
                selection_result.append(pop_ranked[i][0])
    """
    return selection_result


def mating(population, selected):
    """
    :param population:
    :param selected: chosen parent from the selection
    :return: mating pool containing all chosen parents
    """
    mating_result = []
    for i in range(len(selected)):
        mating_result.append(population[selected[i]])
    return mating_result


def crossover(parent1, parent2):
    """
    :param parent1: one parent from the mating pool
    :param parent2: another parent from the mating pool
    :return: offspring of those parents
    """
    child1 = []
    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent2))
    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)
    for i in range(start_gene, end_gene):
        child1.append(parent1[i])
    child2 = [item for item in parent2 if item not in child1]
    child = child1 + child2
    return child


def breed_population(mating_pool):
    """
    :param mating_pool: pool of chosen parents
    :return: new population of the offsprings
    """
    children = []
    length = len(mating_pool) - ELITE_SIZE
    for i in range(ELITE_SIZE):
        children.append(mating_pool[i])
    for i in range(length):
        child = crossover(mating_pool[i], mating_pool[len(mating_pool) - i - 1])
        children.append(child)
    return children


def mutate(route):
    """
    :param route: a single route
    :return: mutated route
    """
    for i in range(len(route)):
        if random.random() < MUTATION_RATE:
            swap_with = int(random.random() * len(route))
            temp = route[i]
            route[i] = route[swap_with]
            route[swap_with] = temp
    return route


def mutate_population(population):
    """
    :param population: all routes from the population pools
    :return: mutated population
    """
    mutate_pop = []
    for i in range(len(population)):
        temp = mutate(population[i])
        mutate_pop.append(temp)
    return mutate_pop
