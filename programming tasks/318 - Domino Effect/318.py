import sys
from operator import itemgetter
import heapq

# -- Build list of systems containing the graphs as adj matrix


def getSystems(input):
    s = []
    i = 0
    while input[i] != (0, 0):  # 0,0 is last system not to be processed
        n = input[i][0]
        m = input[i][1]
        matrix = [[0] * n for j in range(n)]
        for row in input[i + 1:i + 1 + m]:
            matrix[row[1] - 1][row[0] - 1] = row[2]
            matrix[row[0] - 1][row[1] - 1] = row[2]
        s.append(matrix)
        i += m + 1
    return s

# -- Dijkstras algorithm with prev nodes - returns rows like (x,y) x is distance from key 0, y is previous key


def dijkstra(graph):
    dist = [-1] * len(graph[0])
    prev = [-1] * len(graph[0])
    heap = [0]
    dist[0] = 0
    while heap:
        u = heapq.heappop(heap)
        for v in range(len(graph[u])):
            if graph[u][v] > 0:
                q = dist[u] + graph[u][v]
                if q < dist[v] or dist[v] == -1:
                    dist[v] = q
                    prev[v] = u
                    heapq.heappush(heap, v)
    return list(zip(dist, prev))


nr = 0
# -- read input
lines = sys.stdin.readlines()

# -- format input
lines = list(map(lambda x: x.split(), lines))
input = list(map(lambda x: tuple(list(map(int, x))), lines))

systems = getSystems(input)

#calc the results and print in terminal
for system in systems:
    nr += 1
    n = len(system[0])  # number of keys
    dres = dijkstra(system)  # solve shortest path problem with dijkstra
    # print(dres)

    fallLast = max(dres, key=itemgetter(0))  # get latest time at a node
    LastKey = dres.index(fallLast)  # get latest Key Domino

    # Test if last domino falls between two Key Dominos
    LastDomino = -1
    keys = ()
    for u in range(n):

        for v in range(n):

            if(system[u][v] > 0):

                if(v != dres[u][1] and u != dres[v][1]):
                    d = abs(dres[v][0] - dres[u][0])
                    dom = (system[u][v] - d) / 2 + dres[u][0]

                    # last domino falls between keys u and v
                    if(dom > LastDomino and dom > fallLast[0]):
                        LastDomino = dom

                        if(u < v):  # order u and v for output text - smaller key index first
                            keys = (u, v)
                        else:
                            keys = (v, u)

# -- Print Outputs
    print('System #' + str(nr))
    if LastDomino != -1:
        print('The last domino falls after '+str(float(LastDomino)) +
              ' seconds, between key dominoes '+str(keys[0] + 1)+' and '+str(keys[1] + 1)+'.')
    else:
        print('The last domino falls after ' +
              str(float(fallLast[0]))+' seconds, at key domino '+str(LastKey + 1)+'.')
    print('')
