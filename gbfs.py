from collections import defaultdict
from matplotlib import pyplot as plt
import time

heuristics = defaultdict(list)
graph = defaultdict(list)

def addHeuristic(u, v):
    global heuristics
    heuristics[u].append(v)

def addEdge(u, v):
    global graph
    graph[u].append(v)

def print_path(path, start_node, goal_node, finalTime):
    global heuristics
    distance = 0
    print("----------------------------\n| GREEDY BEST FIRST SEARCH |\n----------------------------")
    print("Asal\t\t\t: " + start_node)
    print("Tujuan\t\t\t: " + goal_node)
    print("Waktu\t\t\t: " + str(finalTime))

    for i in path:
        distance += heuristics[i][0]

    print("Kota yang dilewati\t: ", end='')
    for city in path:
        print(city + " -> ", end='') if goal_node != city else print(city)
    print("Jarak\t\t\t:", distance)


def GBFS(start, end):
    global heuristics, graph
    startTime = time.time()
    flag = False
    path = []
    path.append(start)
    while (True):
        if start == end:
            flag = True
            break
        min = 10**7
        for i in graph[start]:
            if heuristics[i][0] < min:
                min = heuristics[i][0]
                start = i
        path.append(start)

    endTime = time.time()
    finalTime = endTime - startTime
    if flag:
        print_path(path, start_node, goal_node, finalTime)
        return path
    else: []

def get_city():
    city = {}
    citiesCode = {}
    f = open("cities.txt")
    j = 1
    for i in f.readlines():
        node_city_val = i.split()
        city[node_city_val[0]] = [int(node_city_val[1]), int(node_city_val[2])]

        citiesCode[j] = node_city_val[0]
        j += 1

    return city, citiesCode

def create_graph():
    graph_actual = {}
    f = open("actuals.txt")
    for i in f.readlines():
        node_val = i.split(",")

        if node_val[0] in graph_actual and node_val[1] in graph_actual:
            c = graph_actual.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph_actual.update({node_val[0]: c})

            c = graph_actual.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph_actual.update({node_val[1]: c})

        elif node_val[0] in graph_actual:
            c = graph_actual.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph_actual.update({node_val[0]: c})

            graph_actual[node_val[1]] = [[node_val[0], node_val[2]]]

        elif node_val[1] in graph_actual:
            c = graph_actual.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph_actual.update({node_val[1]: c})

            graph_actual[node_val[0]] = [[node_val[1], node_val[2]]]

        else:
            graph_actual[node_val[0]] = [[node_val[1], node_val[2]]]
            graph_actual[node_val[1]] = [[node_val[0], node_val[2]]]

    return graph_actual

def draw_map(city, gbfs, graph_actual):
    for i, j in city.items():
        plt.plot(j[0], j[1], "ro")
        plt.annotate(i, (j[0] + 5, j[1]))

        for k in graph_actual[i]:
            n = city[k[0]]
            plt.plot([j[0], n[0]], [j[1], n[1]], "gray")

    for i in range(len(gbfs)):
        try:
            first = city[gbfs[i]]
            scnd = city[gbfs[i + 1]]

            plt.plot([first[0], scnd[0]], [first[1], scnd[1]], "green")
        except: continue

    plt.errorbar(1, 1, label="GBFS", color="green")
    plt.legend(loc="lower right")
    plt.show()

if __name__ == "__main__":
    addHeuristic("Magetan", 162)
    addHeuristic("Surabaya", 0)
    addHeuristic("Ngawi", 130)
    addHeuristic("Ponorogo", 128)
    addHeuristic("Madiun", 126)
    addHeuristic("Bojonegoro", 60)
    addHeuristic("Nganjuk", 70)
    addHeuristic("Jombang", 36)
    addHeuristic("Lamongan", 36)
    addHeuristic("Gresik", 12)
    addHeuristic("Sidoarjo", 22)
    addHeuristic("Probolinggo", 70)
    addHeuristic("Situbondo", 146)
    addHeuristic("Bangkalan", 140)
    addHeuristic("Sampang", 90)
    addHeuristic("Pamekasan", 104)
    addHeuristic("Sumenep", 150)

    addEdge("Magetan", "Ngawi")
    addEdge("Magetan", "Madiun")
    addEdge("Magetan", "Ponorogo")
    addEdge("Surabaya", "Gresik")
    addEdge("Surabaya", "Jombang")
    addEdge("Surabaya", "Bangkalan")
    addEdge("Surabaya", "Sidoarjo")
    addEdge("Ngawi", "Magetan")
    addEdge("Ngawi", "Madiun")
    addEdge("Ngawi", "Bojonegoro")
    addEdge("Ponorogo", "Madiun")
    addEdge("Ponorogo", "Magetan")
    addEdge("Madiun", "Magetan")
    addEdge("Madiun", "Ngawi")
    addEdge("Madiun", "Ponorogo")
    addEdge("Madiun", "Nganjuk")
    addEdge("Bojonegoro", "Ngawi")
    addEdge("Bojonegoro", "Nganjuk")
    addEdge("Bojonegoro", "Jombang")
    addEdge("Bojonegoro", "Lamongan")
    addEdge("Nganjuk", "Madiun")
    addEdge("Nganjuk", "Bojonegoro")
    addEdge("Nganjuk", "Jombang")
    addEdge("Jombang", "Nganjuk")
    addEdge("Jombang", "Bojonegoro")
    addEdge("Jombang", "Surabaya")
    addEdge("Lamongan", "Bojonegoro")
    addEdge("Lamongan", "Gresik")
    addEdge("Gresik", "Lamongan")
    addEdge("Gresik", "Surababaya")
    addEdge("Sidoarjo", "Surabaya")
    addEdge("Sidoarjo", "Probolinggo")
    addEdge("Probolinggo", "Sidoarjo")
    addEdge("Probolinggo", "Situbondo")
    addEdge("Situbondo", "Probolinggo")
    addEdge("Bangkalan", "Surabaya")
    addEdge("Bangkalan", "Sampang")
    addEdge("Sampang", "Bangkalan")
    addEdge("Sampang", "Pamekasan")
    addEdge("Pamekasan", "Sumenep")
    addEdge("Pamekasan", "Sampang")
    addEdge("Sumenep", "Pamekasan")

    graph_actual = create_graph()
    city, citiesCode = get_city()
    start_node = "Magetan"
    goal_node = "Surabaya"
    gbfs = GBFS(start_node, goal_node)
    draw_map(city, gbfs, graph_actual)