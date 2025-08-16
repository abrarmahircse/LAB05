from collections import deque, defaultdict
N, M = map(int, input().split())
graph = defaultdict(list)
in_degree = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

queue = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

count = 0
while queue:
    u = queue.popleft()
    count += 1
    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)
if count == N:
    print("NO")   
else:
    print("YES")  # cycle exists
