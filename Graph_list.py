###############################################################
class Graph:
    """
    Used to define Class Graph: G(V,E)
    """

    def __init__(self):
        self._vertex_list = []
        self._num_vertex = 0
        self._graph = []
        self._index = dict()

    # Add a vertex to the set of vertices and the graph
    def get_num_vertex(self):
        return self._num_vertex

    def get_vertex_list(self):
        return self._vertex_list

    def add_vertex(self, v):
        if v in self._vertex_list:
            print("Vertex ", v, " already exists")
        else:
            self._num_vertex = self._num_vertex + 1
            self._vertex_list.append(v)
            self._index[v.lower()] = self._num_vertex - 1
            if self._num_vertex > 1:
                for vertex in self._graph:
                    vertex.append(0)
            temp = []
            for i in range(self._num_vertex):
                temp.append(0)
            self._graph.append(temp)

    # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2, e):
        # Check if vertex v1 is a valid vertex
        if v1 not in self._vertex_list:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v1 is a valid vertex
        elif v2 not in self._vertex_list:
            print("Vertex ", v2, " does not exist.")
        # Since this code is not restricted to a directed or
        # an undirected graph, an edge between v1 v2 does not
        # imply that an edge exists between v2 and v1
        else:
            index1 = self._vertex_list.index(v1)
            index2 = self._vertex_list.index(v2)
            self._graph[index1][index2] = self._graph[index2][index1] = e

    # Get Graph list as adjacency matrix
    def get_graph(self):
        return self._graph

    # Get edge you want use city's name
    def get_edge_byName(self, v1, v2):
        index1 = self._vertex_list.index(v1)
        index2 = self._vertex_list.index(v2)
        return self._graph[index1][index2]

    # Get edge you want use city's number
    def get_edge_byNumber(self, index1, index2):
        return self._graph[index1][index2]

    # Get the list of the index of the adjacent cities
    def get_list_of_the_index_of_the_adjacent_cities(self, num):
        listOfAdjacentCities = []
        for i in range(self._num_vertex):  # 有多少个城市就执行多少次
            if self._graph[i][num] != 0:  # 逐步检查该列是否相连
                listOfAdjacentCities.append(i)  # 如果相连，则添加到此列表中
        return listOfAdjacentCities

    # Get the index of city in the graph(adjacency matrix)
    def get_index_of_city(self, v):
        if v.lower() not in self._index.keys():
            return -1
        return self._index[v.lower()]

    # Print index of the city
    def print_index(self, v):
        if v.lower() not in self._index.keys():
            print(-1)
        print(self._index[v.lower()])

    # Get the city name based on the index given
    def get_city_name(self, index):
        return self._vertex_list[index]

    # Print the graph directly
    def print_graph(self):
        for i in range(self._num_vertex):
            for j in range(self._num_vertex):
                if self._graph[i][j] != 0:
                    print(self._vertex_list[i], " ———— ", self._vertex_list[j],
                          ", edge weight: ", self._graph[i][j])


def brute_force_solution():
    pass


def dynamic_programming_algorithms():
    pass


def find_the_best_solution():
    pass

