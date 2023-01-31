from collections import deque


def solution(maps):
    width, height = len(maps[0]), len(maps)
    visited = [[0] * width for _ in range(height)]
    visited[0][0] = 1

    def inside(y, x):
        return 0 <= y < height and 0 <= x < width

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if inside(ny, nx) and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    return visited[height - 1][width - 1] or - 1
