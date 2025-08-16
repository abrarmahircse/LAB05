from collections import defaultdict
import sys
sys.setrecursionlimit(2*10**5 + 5)  

n, R = map(int, input().split())
tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)  
subtree_size = [0] * (n+1) 

def dfs(u, parent):#parent is the node from which we came to u
    size = 1  
    for v in tree[u]:
        if v != parent:  # Only recurse into neighbors that are not the parent.
            size += dfs(v, u)
    subtree_size[u] = size
    return size

dfs(R, 0) 
Q = int(input())
for _ in range(Q):
    X = int(input())
    print(subtree_size[X])

