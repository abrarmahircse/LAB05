from collections import deque

R, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

visited = [[False] * H for _ in range(R)]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    diamonds = 0
    if grid[sr][sc] == 'D':
        diamonds += 1
    
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < H:
                if not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    if grid[nr][nc] == 'D':
                        diamonds += 1
    return diamonds

max_diamonds = 0
for i in range(R):
    for j in range(H):
        if not visited[i][j] and grid[i][j] != '#':
            max_diamonds = max(max_diamonds, bfs(i, j))

print(max_diamonds)
