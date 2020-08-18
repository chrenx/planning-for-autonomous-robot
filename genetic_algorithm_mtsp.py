import operator
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fitness import Fitness

POPULATION_SIZE = 10
ELITE_SIZE = 5
MUTATION_RATE = 0.01
# drawing = []


def ga_mtsp(agent_num, city_map_polar, city_maps_matrix, generations):
    """
    :param agent_num: number of agents
    :param city_map_polar: cities represented in terms of xy
    :param generations: generation number
    :param city_maps_matrix: completed graph implemented with adjacency matrix
    """
    final_routes = dict()
    for i in range(agent_num):
        min_route = []
        city_list = [j for j in range(1, len(city_map_polar[i]))]
        pop = initial_population(city_list)
        ranked = rank_routes_by_fitness(pop, city_maps_matrix[i])
        # progress.append(1 / ranked[0][1])
        # print(pop)
        # print("\n")
        # print(ranked)
        print("Initial route for section " + str(i + 1) + ": " + str(pop[ranked[0][0]]))
        print("Initial distance for section " + str(i + 1) + ": " + str(1 / ranked[0][1]))
        min_route.append(pop[ranked[0][0]])
        min_route.append(1 / ranked[0][1])
        for k in range(generations):
            pop = next_generation(pop, city_maps_matrix[i])
            ranked = rank_routes_by_fitness(pop, city_maps_matrix[i])
            if 1 / ranked[0][1] < min_route[1]:
                min_route[0] = pop[ranked[0][0]]
                min_route[1] = 1 / ranked[0][1]
        xy_route = []
        for p in range(len(min_route[0])):
            xy_route.append(city_map_polar[i][min_route[0][p]])
        final_routes[i + 1] = [xy_route, min_route[1]]
    path = []
    for i in range(len(final_routes)):
        path.append(final_routes.get(i + 1)[0])
        print("Best route for section " + str(i + 1) + ": " + str(final_routes.get(i + 1)[0]))
        print("Best distance: " + str(final_routes.get(i + 1)[1]))
    """
    ranked = rank_routes_by_fitness(pop, city_map)
    print("Final distance: " + str(1 / ranked[0][1]))
    best_route_index = rank_routes_by_fitness(pop, city_map)[0][0]
    best_route = pop[best_route_index]
    print("Final route: " + str(best_route))
    """
    """
    plt.plot(drawing)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.savefig('ga_tsp.png')
    """
    print("combine path: " + str(path))
    return path  # best_route


def next_generation(current_generation, city_map):
    """
    :param current_generation: current all routes
    :param city_map: completed graph implemented with adjacency matrix
    :return: next generation of routes
    """
    # global drawing
    pop_ranked = rank_routes_by_fitness(current_generation, city_map)
    # drawing.append(1 / pop_ranked[0][1])
    selected = selection(pop_ranked)
    mating_pool = mating(current_generation, selected)
    children = breed_population(mating_pool)
    next_gener = mutate_population(children)
    return next_gener


def initial_population(city_list):
    """
    :param city_list: list of all the cities represented by number in sequence
    :return: population pool
    """
    population = []
    for i in range(POPULATION_SIZE):
        population.append([0] + random.sample(city_list, len(city_list)))
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
    child2 = []
    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent2))
    while gene_a == 0 or gene_b == 0:  # make sure we keep our starting city
        gene_a = int(random.random() * len(parent1))
        gene_b = int(random.random() * len(parent2))
    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)
    for i in range(start_gene, end_gene):
        child2.append(parent2[i])
    child1 = [item for item in parent1 if item not in child2]
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
    for i in range(1, len(route)):
        if random.random() < MUTATION_RATE:
            swap_with = int(random.random() * len(route))
            while swap_with == 0:
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
