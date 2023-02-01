from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)

    for node, edge in sorted(tickets):
        graph[node].append(edge)

    route, stack = [], ['ICN']

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
