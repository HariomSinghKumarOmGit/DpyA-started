v = 5
edges = [[0,1],[0,3],[2,3],[3,4], [1,4]]

def buildAdjList(v, edges):
    adjList = [[]for i in range(v)]

    for u,v in edges:
        adjList[u].append(v)
        adjList[v].append(u)
    return adjList

print(buildAdjList(v, edges))