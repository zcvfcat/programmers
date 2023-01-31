from collections import deque  # 프로그래머스 링크가 없음;;;;

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우수법


def in_boundary(h, w, y, x):
    return 0 <= y < h and 0 <= x < w


def solution(n, m, hole):
    dp = [[(-1, -1) for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1][0] = 0

    mp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for y, x in hole:
        mp[y][x] = 1

    q = deque()
    q.append((1, 1, 0))

    while q:
        y, x, b = q.popleft()

        for dy, dx in direction:
            for s in range(2):
                if b & s == 1:
                    continue

                ny, nx, nb = dy * (s + 1) + y, dx * (s + 1) + x, b | s

                # if in_boundary()
