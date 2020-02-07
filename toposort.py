#graph is a list of list
#here graph has to be dag
#vertices are numbers starting from zero
#each list shows the vertices that can be reached from corresponding vertex via a directed edge
def toposort(graph):
    visited=[False for v in graph]
    topo=[]
    def utility(v):
        visited[v]=True
        for n in graph[v]:
            if not visited[n]:
                utility(n)
        topo.append(v)

    for v in range(len(graph)):
        if not visited[v]:
            utility(v)
    for i in range(len(topo)):
        print(topo.pop())

g=[
[],
[],
[3],
[1],
[0,1],
[0,2]
]
toposort(g)
