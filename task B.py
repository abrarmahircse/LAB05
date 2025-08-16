import sys
sys.setrecursionlimit(2*10**5 + 5)
from collections import defaultdict

n, m = map(int, input().split())

u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(m):
    u = u_list[i]
    v = v_list[i]
    graph[u].append(v)
    graph[v].append(u)  

# DFS
visited = set()
dfs_order = []

def DFS(u):
    visited.add(u)
    dfs_order.append(u)
    for v in graph[u]:
        if v not in visited:
            DFS(v)

DFS(1)
print(*dfs_order)
