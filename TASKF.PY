from collections import defaultdict
import sys
sys.setrecursionlimit(2*10**5 + 5)

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)  

visited = [False] * (n+1)
rec_stack = [False] * (n+1)

def dfs(u):
    visited[u] = True
    rec_stack[u] = True
    for v in graph[u]:
        if not visited[v]:
            if dfs(v):
                return True
        elif rec_stack[v]:
            return True  # cycle 
    rec_stack[u] = False  # remove from recursion stack
    return False

found_cycle = False
for node in range(1, n+1):
    if not visited[node]:
        if dfs(node):
            found_cycle = True
            break

if found_cycle:
    print("YES")
else:
    print("NO")
