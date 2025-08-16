from collections import deque

# 1. Read  vertices (n) and edges (m)
n, m = map(int, input().split())

# 2. Create an adjacency list (graph)
graph = {i: [] for i in range(1, n+1)}

# 3. Read all edges
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)   # since it's undirected

# 4. BFS function
def bfs(start):
    visited = set()       # keeps track of visited nodes
    Q = deque([start])    # initialize queue with the start node
    visited.add(start)    # mark start as visited
    
    while Q:              # while queue is not empty
        u = Q.popleft()   # dequeue
        print("Visiting:", u)
        
        for v in graph[u]:    # go through all neighbors
            if v not in visited:
                visited.add(v)
                Q.append(v)
    
    return visited

# 5. Run BFS from node 1
bfs(1)

""" 6 7
1 2
1 3
2 4
2 5
3 6
5 6
4 5 """




""" BFS(G,s):
for each vertex u in G.V:
u.colour = 0
Q =Ø;
s.colour = 1
ENQUEUE (Q,s)
while Q 0;
u = DEQUEUE (Q)
for each v in G.Adj[u]:
if v.colour == 0:
v.colour = 1
ENQUEUE (Q,v)  shift alt A """


