import time, heapq

class priority_queue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        return True if self.cities == [] else False

    def check(self):
        print(self.cities)

class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)

jatim = {}
def makedict():
    f = open("actuals.txt")
    for line in f.readlines():
        word = line.split()
        ct1 = word[0]
        ct2 = word[1]
        dist = int(word[2])
        jatim.setdefault(ct1, []).append(ctNode(ct2, dist))
        jatim.setdefault(ct2, []).append(ctNode(ct1, dist))

def get_heuristics():
    h = {}
    with open("heuristics.txt", 'r') as f:
        for line in f:
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
    q = priority_queue()
    h = get_heuristics()

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

    print("---------------------------\n|\t A* SEARCH\t   |\n---------------------------")
    print("Asal\t\t\t\t: " + start)
    print("Tujuan\t\t\t\t: " + end)
    print("Kota yg dilewati\t\t:", finalpath)
    print("Jumlah kota yang dilewati \t:", len(finalpath))
    print("Total jarak \t\t\t:", distance[end])
    print("Waktu\t\t\t\t:", finalTime)

if __name__ == "__main__":
    src = "Magetan"
    dst = "Surabaya"
    makedict()
    astar(src, dst)
