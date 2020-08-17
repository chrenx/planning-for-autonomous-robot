from Graph_list import Graph
import random
import time
from dynamic_programming import dynamic_programming_tsp
from brutal_force import brutal_force_single_tsp
from greedy_algorithm import greedy_algorithm


def generate_random_different_adjacent_matrix(cities_number):
    num_list = [[0] * cities_number for i in range(cities_number)]
    for j in range(cities_number):
        for k in range(cities_number):
            num_list[j][k] = num_list[k][j] = random.randint(10, 99)

    for m in range(cities_number):
        num_list[m][m] = 0

    return num_list


# Driver Code
if __name__ == "__main__":
    temp = Graph()
    temp.print_graph()
    temp_graph = temp.get_graph()

    # Add vertices to the graph
    temp.add_vertex("Grand Rapids")
    temp.add_vertex("Saginaw")
    temp.add_vertex("Kalamazoo")
    # temp.add_vertex("Detroit")
    # temp.add_vertex("Toledo")

    # Add the edges between the vertices by specifying
    # the from and to vertex along with the edge weights.
    temp.add_edge("Grand Rapids", "Saginaw", 113)
    # temp.add_edge("Grand Rapids", "Detroit", 147)
    # temp.add_edge("Grand Rapids", "Toledo", 167)
    temp.add_edge("Grand Rapids", "Kalamazoo", 56)
    temp.add_edge("Saginaw", "Kalamazoo", 137)
    # temp.add_edge("Saginaw", "Toledo", 142)
    # temp.add_edge("Saginaw", "Detroit", 98)
    # temp.add_edge("Kalamazoo", "Detroit", 135)
    # temp.add_edge("Kalamazoo", "Toledo", 133)
    # temp.add_edge("Toledo", "Detroit", 58)
    # print("Internal representation: ", temp_graph)

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

    # greedy_algorithm(temp, start_city)  # 使用Greedy_Algorithm
