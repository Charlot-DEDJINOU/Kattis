from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
in_degree = [0] * (n + 1)

# Lire les paires a, b
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    in_degree[a] += 1

# Initialiser la liste des bâtons pouvant être ramassés
can_pick = [i for i in range(1, n + 1) if in_degree[i] == 0]

# Parcourir les bâtons
picked_order = []
while can_pick:
    b = can_pick.pop(0)
    picked_order.append(b)
    for a in graph[b]:
        in_degree[a] -= 1
        if in_degree[a] == 0:
            can_pick.append(a)

# Si tous les bâtons ont été ramassés, afficher l'ordre
if len(picked_order) == n:
    for b in reversed(picked_order):
        print(b)
else:
    print("IMPOSSIBLE")