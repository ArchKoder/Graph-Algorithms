#graph is a list of dictionaries
#each list index corresponds to a vertex
#and dictionary at the index of list corresponds to neighbouring nodes and weights
#undirected graph or directed doesn't matter
from heapq import heapify
from heapq import heappop as hpop
graph=[
{1:2,2:3},
{0:2,2:1,3:1,4:4},
{0:3,1:1,5:5},
{1:1,4:1},
{1: 4, 3: 1, 5: 1},
{2:5,4:1,6:1},
{5:1}
]
def kruskal(graph):
    edges=[]
    for v in range(len(graph)):
        for n,e in graph[v].items():
            edges.append((e,min(n,v),max(n,v)))
    edges=list(set(edges))
    g=[]
    heapify(edges)
    visited=[False for i in graph]
    while edges:
        e=hpop(edges)
        if not visited[e[1]] or not visited[e[2]]:
            visited[e[1]]=visited[e[2]]=True
            g.append(e)
    print(g)
kruskal(graph)
