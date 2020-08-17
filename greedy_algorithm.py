from Graph_list import Graph

def greedy_algorithm(temp, start_city):
    graph = Graph()
    graph = temp
    print("Using Greedy_Algorithm")
    print("#####################################################################")
    N = graph.get_num_vertex()
    list = graph.get_vertex_list()
    visit = [0] * N
    for i in range(0, N-1):
        visit[i] = 0
    path = []
    path.append(start_city)
    global start
    start1 = graph.get_index_of_city(start_city)
    start = graph.get_index_of_city(start_city)
    visit[start] = 1
    matrix = graph.get_graph()
    global dis

    global cost
    cost = 0
    for i in range(0,N-1):
        dis = 1000
        for j in range(0,N):
            if(visit[j] == 0 and matrix[start][j]< dis):
                dis = matrix[start][j]
                k = j

        start = k
        cost = cost+dis
        visit[start] = 1;
        city = graph.get_city_name(start)
        path.append(city)

    city1 = graph.get_index_of_city(path[4])
    cost = cost + matrix[start1][city1]
    path.append(start_city)
    print("Shortest route: ")
    #for i in range(0,N-2):
    #    print(path[i],"--->")
    #print(path[4])
    print(path)
    print("the cost is:",cost)






