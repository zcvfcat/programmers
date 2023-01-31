def dfs(k, graph, visited):
    visited[k] = 1

    for i in range(len(graph[k])):
        if visited[i] == 0 and graph[k][i] == 1:
            dfs(i, graph, visited)


def solution(n, computers):
    visited = [0 for _ in range(n)]
    ans = 0

    for i in range(n):
        if visited[i] == 0:
            dfs(i, computers, visited)
            ans += 1

    return ans
