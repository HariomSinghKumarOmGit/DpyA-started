
 # copunt no os componenets of a graph

v = 10
edges = [
    [0,1],
    [0,2],
    [1,2],
    [2,3],
    [4,5],
    [6,7],
    [6,8],
    [7,8],
    [9,4]
]



adjList = buildAdjList(v, edges)
visited = [False]*v
ans = 0
 
for i in range(v):
    if not visited[i]:
        dfs(adjlist,i,visited)
        ans+=1

print (ans)