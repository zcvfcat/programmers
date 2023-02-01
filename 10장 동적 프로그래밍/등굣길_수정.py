def dfs(y, x, dp, puddles):
    row, col = len(dp), len(dp[0])
    path = [[1, 0], [0, 1]]

    def inside(y, x):
        return 0 <= y < col and 0 <= x < row

    if [y, x] == [row - 1, col - 1]:
        return 1

    if dp[y][x] != 0:
        return dp[y][x]

    for dy, dx in path:
        ny, nx = y + dy, x + dx

        if inside(ny, nx) and not ([ny + 1, nx + 1] in puddles):
            answer += dfs(ny, nx, dp, puddles)

    return dp[y][x] % 1000000007


def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]

    return dfs(0, 0, dp, puddles)
