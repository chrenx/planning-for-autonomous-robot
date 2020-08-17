from Graph_list import Graph
import math
import numpy as np
import random
#import matplotlib.pyplot as plt
global dis
global cost

global T_min  # 温度的下限，若温度T达到T_min，则停止搜索


def Simulated_Annealing(temp, start_city):
    global r  # 用于控制降温的快慢
    global T # 系统的温度
    global N
    r = 0.99999


    global graph
    graph = Graph()
    graph = temp
    global start
    start = graph.get_index_of_city(start_city)
    global matrix
    global list
    N = graph.get_num_vertex()
    matrix = graph.get_graph()
    list = graph.get_vertex_list()
    list1 =[]
    for i in range (0,N):
        list1.append(list[i])
    list1.remove(start_city)
    list1.insert(0,start_city)
    global indexlist

   # print(list1)
    indexlist=graph.get_index(list1)
    indexl = []
    for i in range (0,N):
        indexl.append(indexlist[i])

    print("Using Simulated_Annealing")
    print("#####################################################################")
   # cost = np.sum(matrix(start))
   # visit = [0] * N
   # for i in range(0, N-1):
     #   visit[i] = 0
 #   path = []
  #  path.append(start_city)
  #  visit[start] = 1

    path = []

   # print(indexlist)
    city11 = graph.get_city_name(4)
   # print(city11)
   # cost = 0
    T = 10**10
    T_min = 1
    t = 0
    while T > T_min:
        index = new_path(indexl)
        dE = cost(indexl,N)-cost(index,N)
        if dE > 0:
            indexl = index
        else:
            if math.exp(dE / T) > random.uniform(0, 1):
               indexl = index
        T = T * r

        t+=1

    #print(indexl)
   # path = graph.getcity(indexlist)
    city = []

    for i in range(0, N):
        city.append(graph.get_city_name(indexl[i]))
    city.append(city[0])

    cost1 = cost(indexl,N)

    print("Shortest route: ")
    #for i in range(0,N-2):
    #    print(path[i],"--->")
    #print(path[4])
    print(city)
    print("the cost is:",cost1)
    print(t)
   # plt.plot(np.array(cost1))

def cost(indexlist,N):
    cost = 0
    j = N
    for i in range (0,N-1):
        cost += matrix[indexlist[i]][indexlist[i+1]]
    cost += matrix[indexlist[j-1]][indexlist[0]]
    return cost

def new_path(indexl):
    i = random.randint(1, 4)
    j = random.randint(1, 4)
    a = random.randint(1,2)
    if a == 1:
    #print(indexlist[i])
        x = indexl[i]
        indexl[i] = indexl[j]
        indexl[j] = x
        return indexl

    else:
        ind = []
        for n in range(1,N):
            ind.append(indexl[n])
        ind.reverse()
        ind.insert(0,indexl[0])
        return ind
























