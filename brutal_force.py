from Graph_list import Graph

routes = []
whole_map = Graph()


def brutal_force_single_tsp(temp, start_city):
    print("Using Brutal force method(BF-method)")
    print("#####################################################################")
    global whole_map
    whole_map = temp
    cost = 0
    path = []
    start = whole_map.get_city_name(whole_map.get_index_of_city(start_city))
    path.append(start)
    graph = whole_map.get_graph()
    help_method(start, graph, path, cost)

    routes.sort()
    print(routes)
    if len(routes) != 0:
        print("Shortest route: ", routes[0][1], "of which cost is: ", routes[0][0])
    else:
        print("FAILLLL!")


def help_method(node, graph, path, cost):
    city_index = whole_map.get_index_of_city(node)
    if node not in path:
        path.append(node)
    if len(path) > 1:
        cost += graph[whole_map.get_index_of_city(path[-2])][city_index]
    if (len(graph) == len(path)) and (graph[whole_map.get_index_of_city(path[-1])]
                                      [whole_map.get_index_of_city(path[0])] != 0):
        global routes
        path.append(path[0])
        cost += graph[whole_map.get_index_of_city(path[-2])][
            whole_map.get_index_of_city(path[0])]
        routes.append([cost, path])
        return
    for i in range(len(graph)):
        city = whole_map.get_city_name(i)
        if (city not in path) and (graph[i][city_index] != 0):
            help_method(city, graph, list(path), cost)
