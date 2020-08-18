import random
import time
import genetic_algorithm
import genetic_algorithm_mtsp
import math
from city_polar import City
from Graph_list import Graph
from dynamic_programming import dynamic_programming_tsp
from brutal_force import brutal_force_single_tsp
from greedy_algorithm import greedy_algorithm

# agents# > 1
# cities# < agents#
CITY_NUM = 40
AGENT_NUM = 5
# SECTION_LIMIT = int((CITY_NUM - 1) / AGENT_NUM)  # 4 in this case
SECTION_DEGREE = 360 / AGENT_NUM
"""
def generate_random_different_adjacent_matrix(cities_number):
    num_list = [[0] * cities_number for i in range(cities_number)]
    for j in range(cities_number):
        for k in range(cities_number):
            num_list[j][k] = num_list[k][j] = random.randint(10, 99)

    for m in range(cities_number):
        num_list[m][m] = 0

    return num_list
"""


def random_city_polar_coordinate():
    original = City(0, 0)
    polar = dict()
    count_city_added = 0
    section_index = 0
    while count_city_added < CITY_NUM - 1:  # leave one spot for original
        r = random.uniform(0, 200)
        start = section_index * SECTION_DEGREE
        end = section_index * SECTION_DEGREE + SECTION_DEGREE
        theta = random.uniform(start, end)
        while r == 0:
            r = random.uniform(0, 200)
        temp = City(r, theta)
        if section_index not in polar:
            polar[section_index] = [original, temp]
        else:
            polar[section_index].append(temp)
        if section_index == AGENT_NUM - 1:
            section_index = 0
        else:
            section_index += 1
        count_city_added += 1

    result = []
    for i in range(len(polar)):
        result.append(polar[i])
    return result


def generate_city_map_matrix(map_polar):
    results = []
    for i in range(AGENT_NUM):
        a = map_polar[i]
        num_list = [[0] * len(a) for i in range(len(a))]
        for j in range(len(a)):
            for k in range(j, len(a)):
                num_list[j][k] = num_list[k][j] = a[j].get_distance(a[k])
        results.append(num_list)
    return results


# Driver Code
if __name__ == "__main__":
    city_map_polar = random_city_polar_coordinate()  # [[(,), (,)], [(,), (,)]]
    city_map_matrix = generate_city_map_matrix(city_map_polar)


    start = time.time()
    genetic_algorithm_mtsp.ga_mtsp(AGENT_NUM, city_map_polar, city_map_matrix, 500)
    end = time.time()
    print("Timing: " + str(end - start))

    # Genetic Algorithm on TSP
    """
    city_list = [i for i in range(CITY_NUM)]
    city_map = generate_random_different_adjacent_matrix(CITY_NUM)
    # fixed_map = [[0, 72, 54, 53], [72, 0, 16, 17], [54, 16, 0, 61], [53, 17, 61, 0]]
    start = time.time()
    genetic_algorithm.ga_tsp(city_list, city_map, 500)  # city_num = 20
    end = time.time()
    print("Timing: " + str(end - start))
    """

    """
    temp = Graph()
    temp.print_graph()
    temp_graph = temp.get_graph()
    # Add vertices to the graph
    temp.add_vertex("Grand Rapids")
    temp.add_vertex("Saginaw")
    temp.add_vertex("Kalamazoo")
    temp.add_vertex("Detroit")
    temp.add_vertex("Toledo")
    # Add the edges between the vertices by specifying
    # the from and to vertex along with the edge weights.
    temp.add_edge("Grand Rapids", "Saginaw", 113)
    temp.add_edge("Grand Rapids", "Detroit", 147)
    temp.add_edge("Grand Rapids", "Toledo", 167)
    temp.add_edge("Grand Rapids", "Kalamazoo", 56)
    temp.add_edge("Saginaw", "Kalamazoo", 137)
    temp.add_edge("Saginaw", "Toledo", 142)
    temp.add_edge("Saginaw", "Detroit", 98)
    temp.add_edge("Kalamazoo", "Detroit", 135)
    temp.add_edge("Kalamazoo", "Toledo", 133)
    temp.add_edge("Toledo", "Detroit", 58)
    print("Internal representation: ", temp_graph)
    """

    """
    start_city = input("Enter the city you want to start:")
    start_index = temp.get_index_of_city(start_city.lower())

    # check if the city typed by user is in the list
    if start_index == -1:
        print("City does not exist!")
    else:
        print("You want to begin with the city: " + start_city + ", whose index is: ",
              start_index, ".")
    brutal_force_single_tsp(temp, start_city)  # 使用BF-method
    """

    """
    print("#####################################################################")
    n = generate_random_different_adjacent_matrix(11)
    # for item in n:
    #    print(item)
    print(n)
    start = time.time()
    dynamic_programming_tsp(n, 0)
    end = time.time()
    print(str(end - start))
    print("#####################################################################")
    """

    # greedy_algorithm(temp, start_city)  # 使用Greedy_Algorithm
