from collections import deque
n, m = map(int, input().split())

graph = {i: [] for i in range(1, n+1)} #adjacency list
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # UNDIRECTED  

def bfs(start):
    visited = set()
    Q = deque([start])
    visited.add(start)
    result = []  
    
    while Q:
        u = Q.popleft()
        result.append(u)  
        
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                Q.append(v)
    
    print(*result) 
bfs(1)

