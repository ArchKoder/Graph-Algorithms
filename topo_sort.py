from collections import defaultdict
class Graph():
    """directed graph with no weight"""
    def __init__(self,v=0):
        self.V=v
        self.to=[]
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

def topo(g):
    for node in range(g.V):
        if node not in g.to:
            hope=True
            for k in g.graph.keys():
                if node in g.graph[k]:
                    hope=False
            if hope:
                g.graph[node]=[]
                g.to.append(node)
                return (g)

def topo_sort(g):
    temp=Graph(g.V)
    temp.graph=g.graph.copy()
    for i in range(g.V):
        temp=topo(temp)
    g.to=temp.to

g=Graph(6)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(4,1)
g.addEdge(4,0)
g.addEdge(5,2)
g.addEdge(5,0)

topo_sort(g)
print(g.to)
