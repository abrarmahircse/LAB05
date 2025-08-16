import sys # in buuilt sort used 
from collections import deque

sys.setrecursionlimit(2*10**5 + 5)
input = sys.stdin.readline  # faster input for CP

def main():
    n, m, S, D = map(int, input().split())
    u_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = u_list[i], v_list[i]
        graph[u].append(v)
        graph[v].append(u)

    
    for i in range(1, n + 1):
        if graph[i]:
            graph[i].sort()

    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    q = deque([S])
    dist[S] = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
    if dist[D] == -1:
        print(-1)
    else:
        path = []
        cur = D
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        print(dist[D])
        print(*path)


main()