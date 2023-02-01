def solution(n, computers):
    parents = [i for i in range(n)]

    def find(node):
        if node != parents[node]:
            parents[node] = find(parents[node])
        return parents[node]

    def union(node_a, node_b):
        node_a = find(node_a)
        node_b = find(node_b)

        if node_a != node_b:
            parents[node_b] = node_a

    for node, edges in enumerate(computers):
        for edge, value in enumerate(edges):
            if node != edge and value == 1:
                union(node, edge)

    return len(set(map(lambda x: find(x), parents)))
