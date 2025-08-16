import sys
sys.setrecursionlimit(10**6)  

R, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

visited = [[False]*H for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x < 0 or x >= R or y < 0 or y >= H:
        return 0
    if visited[x][y] or grid[x][y] == '#':
        return 0

    visited[x][y] = True
    diamonds = 1 if grid[x][y] == 'D' else 0

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        diamonds += dfs(nx, ny)   
    return diamonds
max_diamonds = 0

for i in range(R):
    for j in range(H):
        if not visited[i][j] and grid[i][j] != '#':
            max_diamonds = max(max_diamonds, dfs(i, j))

print(max_diamonds)
