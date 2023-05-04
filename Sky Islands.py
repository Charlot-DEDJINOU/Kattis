def dfs(at, visited, graph):
    visited[at] = True
    for neighbor in graph[at]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

def is_connected(n, m, graph):
    visited = [False] * n
    dfs(0, visited, graph)
    for i in range(n):
        if not visited[i]:
            return False
    return True

n, m = map(int, input().split())
graph = {i: [] for i in range(n)}
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

if is_connected(n, m, graph):
    print("YES")
else:
    print("NO")