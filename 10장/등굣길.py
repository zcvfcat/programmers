# 실패하는게 정상이라고 함

def dfs(y, x, row, col, puddles):
    path = [[1, 0], [0, 1]]
    answer = 0

    def inside(y, x):
        return 0 <= y < col and 0 <= x < row

    if [y, x] == [row - 1, col - 1]:
        return 1

    for dy, dx in path:
        ny, nx = y + dy, x + dx

        if inside(ny, nx) and not ([ny + 1, nx + 1] in puddles):
            answer += dfs(ny, nx, row, col, puddles)

    return answer % 1000000007


def solution(m, n, puddles):
    return dfs(0, 0, n, m, puddles)
