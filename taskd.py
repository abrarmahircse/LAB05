from collections import defaultdict, deque
n, m, S, D, K = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) # directed 

def bfs_path(start, end):
    visited = set()
    parent = {}
    queue = deque([start])
    visited.add(start)
    
    while queue:
        u = queue.popleft()
        if u == end:
            path = []
            cur = end
            while cur != start:
                path.append(cur)
                cur = parent[cur]
            path.append(start)
            path.reverse()
            return path
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)
    return None  

#S to K
path1 = bfs_path(S, K)
if not path1:
    print(-1)
    exit()
#K to D
path2 = bfs_path(K, D)
if not path2:
    print(-1)
    exit()

full_path = path1 + path2[1:]
print(len(full_path)-1)
print(*full_path)
