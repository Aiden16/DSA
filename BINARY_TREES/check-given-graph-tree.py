from pydoc import visiblename


n = int(input())
edges = []
for i in range(n-1):
    e = list(map(int,input().split(' ')))
    edges.append(e)
global visited,adj
visited = set()
adj = {i:[] for i in range(n)}
print(adj)
for n1,n2 in edges:
    adj[n1].append(n2)
    adj[n2].append(n1)
def dfs(prev,node):
    if node in visited:
        return False
    visited.add(node)
    for j in adj[node]:
        if j == prev:
            continue
        if not dfs(node,j):
            return False
    return True
x = dfs(-1,0)
print(x,visited)   
