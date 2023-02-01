from collections import deque


def solution(board):
    size = len(board)
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def inside(y, x):
        return 0 <= y < size and 0 <= x < size

    def bfs(start_y, start_x, cost, path):
        graph = [[0 for _ in range(len(size))] for _ in range(size)]
        for y in range(size):
            for x in range(size):
                if board[y][x] == 1:
                    graph[y][x] = -1

        q = deque((y, x, cost, path))

        while q:
            y, x, cost, path = q.popleft()

            for dy, dx, i in enumerate(direction, 1):
                ny, nx = dy + y, dx + x

                if inside(ny, nx) and graph[ny][nx] is not - 1:
                    newcost = cost + 100 if path == i else cost + 600

                    if graph[ny][nx] == 0 or (graph[ny][nx] != 0 and graph[ny][nx] > newcost):
                        q.append((ny, nx, newcost, i))
                        graph[ny][nx] = newcost
        return graph[size - 1][size - 1]

    return min(bfs(0, 0, 0, 2), bfs(0, 0, 0, 3))
