import heapq
def dijkstra(graph,src):
    dijk={v:float('inf') for v in graph}
    dijk[src]=0

    q=[(0,src)]
    while len(q):
        d,v=heapq.heappop(q)
        if dijk[v]<d:
            continue
        for n,w in graph[v].items():
            t=d+w
            if t<dijk[n]:
                dijk[n]=t
                heapq.heappush(q,(t,n))
    return dijk
graph={
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(dijkstra(graph,'X'))
