from collections import deque


def solution(n, edge):
    answer = 0
    route = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    q = deque()

    for vertex, adj_vertex in edge:
        graph[vertex] += adj_vertex
        graph[adj_vertex] += vertex

    q.append(1)
    route[1] = 1

    while q:
        node = q.popleft()

        for edge in graph[node]:
            if route[edge] == 0:
                q.append(edge)
                route[edge] = route[node] + 1

    max_edge = max(route)

    for r in route:
        if r == max_edge:
            answer += 1

    return answer
