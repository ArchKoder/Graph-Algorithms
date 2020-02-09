def kosaraju(graph):
    s,visited=[],[False for l in graph]
    def utility(v):
        visited[v]=True
        for n in graph[v]:
            if not visited[n]:
                utility(n)
        s.append(v)
    def transpose(graph):
        g=[[]for l in graph]
        for i in range(len(g)):
            for j in graph[i]:
                g[j].append(i)
        return g
    g=transpose(graph)
    def utility2(v):
        visited[v]=True
        print(v,end=", ")
        for n in g[v]:
            if not visited[n]:
                utility2(n)
    for v in range(len(graph)):
        if not visited[v]:
            utility(v)
    g=transpose(graph)
    visited=[False for l in graph]

    while(s):
        v=s.pop()
        if not visited[v]:
            utility2(v)
            print("")

graph=[
[2,3],
[0],
[1],
[4],
[]
]
kosaraju(graph)
