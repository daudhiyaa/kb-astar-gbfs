import time
import heapq

class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False


    def check(self):
        print(self.cities)


class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)


jatim = {}

def makedict():
    file = open("actuals.txt", 'r')
    for string in file:
        line = string.split(',')
        ct1 = line[0]
        ct2 = line[1]
        dist = int(line[2])
        jatim.setdefault(ct1, []).append(ctNode(ct2, dist))
        jatim.setdefault(ct2, []).append(ctNode(ct1, dist))

def makehuristikdict():
    h = {}
    with open("heuristics.txt", 'r') as file:
        for line in file:
            line = line.strip().split()
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h


def heuristic(node, values):
    return values[node]


def astar(start, end):
    startTime = time.time()
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in jatim[current]:
            g_cost = distance[current] + int(new.distance)

            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current

    endTime = time.time()
    finalTime = endTime - startTime
    printoutput(start, end, path, distance, finalTime)


def printoutput(start, end, path, distance, finalTime):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()

    print("----------------------------\n| A* SEARCH |\n----------------------------")
    print("Asal\t\t\t\t\t: " + start)
    print("Tujuan\t\t\t\t\t: " + end)
    print("Kota yg dilewati dg jarak terpendek\t: " + str(finalpath))
    print("Jumlah kota yang dilewati \t\t: " + str(len(finalpath)))
    print("Total jarak \t\t\t\t: " + str(distance[end]))
    print("Waktu\t\t\t\t\t: " + str(finalTime))


def main():
    src = "Magetan"
    dst = "Surabaya"
    makedict()
    astar(src, dst)


if __name__ == "__main__":
    main()
