from collections import defaultdict


# F n =vertices,m edges
n, m = map(int, input().split())

# Build adjacency list
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)   # remove this line if graph is directed

# ---- DFS with visited ----
visited = set()
dfs_order = []   # record traversal order

def DFS(u):
    visited.add(u)         # mark as visited
    dfs_order.append(u)    # record discovery
    for v in graph[u]:     # go through neighbors
        if v not in visited:
            DFS(v)

# ---- Run DFS on all vertices ----
for u in range(1, n+1):
    if u not in visited:   # ensure disconnected components are covered
        DFS(u)

# ---- Output ----
print("DFS traversal order:", dfs_order)



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
ENQUEUE (Q,v) """