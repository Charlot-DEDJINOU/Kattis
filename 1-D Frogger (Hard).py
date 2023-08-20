import sys
sys.setrecursionlimit(2*10**5)
from collections import Counter

def main():
    n = int(input())
    values = list(map(int, input().split()))

    outgoing_edges, incoming_edges = {}, {}
    for i in range(n):
        if 0 <= i + values[i] < n:
            if i not in outgoing_edges:
                outgoing_edges[i] = []
            if i + values[i] not in incoming_edges:
                incoming_edges[i + values[i]] = []
            outgoing_edges[i].append(i + values[i])
            incoming_edges[i + values[i]].append(i)

    def topological_sort(graph, nodes=range(n)):
        result = []
        visited = set()
        
        def dfs(node):
            visited.add(node)
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor)
            result.append(node)
        
        for i in nodes:
            if i not in visited:
                dfs(i)
        
        return result

    sorted_nodes = topological_sort(outgoing_edges)

    scc_labels, visited, current_label = [-1] * n, [0] * n, 0
    def assign_scc_label(node):
        visited[node], scc_labels[node] = 1, current_label
        if node in incoming_edges:
            for neighbor in incoming_edges[node]:
                if not visited[neighbor]:
                    assign_scc_label(neighbor)

    for node in sorted_nodes[::-1]:
        if not visited[node]:
            assign_scc_label(node)
            current_label += 1

    scc_values = {}
    scc_count = {}
    scc_count_duplicate = {}
    for i, label in enumerate(scc_labels):
        if label not in scc_count:
            scc_count[label], scc_count_duplicate[label] = set(), []
        scc_count[label].add(values[i])
        scc_count_duplicate[label].append(values[i])

    scc_graph = {}
    scc_connections = set()
    for node in outgoing_edges:
        for neighbor in outgoing_edges[node]:
            if scc_labels[node] != scc_labels[neighbor]:
                scc_graph[scc_labels[node]] = [scc_labels[neighbor]]
                scc_connections.add(scc_labels[node])
                scc_connections.add(scc_labels[neighbor])

    scc_reverse_graph = {}
    for node in scc_graph:
        if scc_graph[node][0] not in scc_reverse_graph:
            scc_reverse_graph[scc_graph[node][0]] = set()
        scc_reverse_graph[scc_graph[node][0]].add(node)

    sorted_scc = topological_sort(scc_graph, scc_connections)

    visited_scc, visited_count = set(), {}
    answer = [0]
    def dfs_scc(node):
        visited_scc.add(node)
        if node in scc_reverse_graph:
            for neighbor in scc_reverse_graph[node]:
                magnitude = scc_count_duplicate[neighbor][0]
                answer[0] += len(visited_count) - (magnitude in visited_count)
                visited_count[magnitude] += 1
                dfs_scc(neighbor)
                visited_count[magnitude] -= 1
                if visited_count[magnitude] == 0:
                    del visited_count[magnitude]

    for scc_label in sorted_scc:
        if scc_label not in visited_scc:
            visited_count = Counter(scc_count[scc_label])
            dfs_scc(scc_label)

    final_answer = answer[0] + sum(len(scc_count[label]) * len(scc_count_duplicate[label]) for label in scc_count)
    print(final_answer)

if __name__ == "__main__":
    main()