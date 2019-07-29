from collections import defaultdict
class Graph():
    """directed graph with no weight"""
    def __init__(self,v=0):
        self.V=v
        self.to=[]
        self.graph=defaultdict(list)
        self.w=[[0 for _ in range(self.V)]for _ in range(self.V)]

    def addEdge(self,u,v,w):
        self.graph[u].append(v)
        self.w[u][v]=w
        self.w[v][u]=w

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
g.addEdge(0, 1, 5);
g.addEdge(0, 2, 3);
g.addEdge(1, 3, 6);
g.addEdge(1, 2, 2);
g.addEdge(2, 4, 4);
g.addEdge(2, 5, 2);
g.addEdge(2, 3, 7);
g.addEdge(3, 5, 1);
g.addEdge(3, 4, -1);
g.addEdge(4, 5, -2);
topo_sort(g)
d=[float('-inf')]*g.V
d[g.to[0]]=0
for u in g.to:
    for v in g.graph[u]:
        d[v]=max(d[v],d[u]+g.w[u][v])
print("longest path from",g.to[0],"has length",max(d))
