#🔹 Case 1: Multiple test cases, always start from node 1
from collections import deque

def bfs(graph, start):
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

# -----------------------------
t = int(input())  # number of test cases
for _ in range(t):
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n+1)}
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # undirected
    
    bfs(graph, 1)  # always start from node 1

#Case 2: Multiple test cases, start node is given in input
from collections import deque

def bfs(graph, start):
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

# -----------------------------
t = int(input())  # number of test cases
for _ in range(t):
    n, m, s = map(int, input().split())  # notice: source node `s` given
    graph = {i: [] for i in range(1, n+1)}
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # undirected
    
    bfs(graph, s)  # start from given source node
