import sys
from collections import deque

sys.setrecursionlimit(2*10**5 + 5)
input = sys.stdin.readline 

def merge(arr):
    n = len(arr)
    width = 1
    result = arr[:]
    while width < n:
        for i in range(0, n, 2 * width):
            left, right = i, min(i + width, n)
            mid, end = right, min(i + 2 * width, n)
            merged = []
            l, r = left, mid
            while l < mid and r < end:
                if result[l] <= result[r]:
                    merged.append(result[l]); l += 1
                else:
                    merged.append(result[r]); r += 1
            while l < mid:
                merged.append(result[l]); l += 1
            while r < end:
                merged.append(result[r]); r += 1
            result[left:end] = merged
        width *= 2
    return result


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
            graph[i] = merge(graph[i])

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


if __name__ == "__main__":
    main()
