v = 5
edges = [[0,1],[0,3],[2,3],[3,4], [1,4]]

def buildAdjMatrix (v, edges):
    adjMatrix = [[0 for j in range(v)]for i in range(v)]

    for u,v in edges:
        adjMatrix[u][v] = 1
        adjMatrix[u][v] = 1
        
    return adjMatrix

adjMatrix = buildAdjMatrix (v, edges)
for i in adjMatrix:
    for j in i :
        print (j , end= " ")
    print()