from collections import defaultdict
class Graph():
    def __init__(self,v=0):
        self.V=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

def detect_cycle(g):
    visited=[False]*g.V
    s=[]
    for v in range(g.V):
        if len(g.graph[v])>0:
            s.append(v)
            break
    while(len(s)>0):
        node=s.pop()
        if not visited[node]:
            visited[node]=True
        else:
            return True
        for i in g.graph[node]:
            s.append(i)
    return False

g=Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(detect_cycle(g))


g=Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(3,4)
print(detect_cycle(g))
