def solution(board, skill):
    answer = 0
    temp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for attack_type, r1, c1, r2, c2, degree in skill:
        degree *= -1 if attack_type == 1 else 1
        temp[r1][c1] += degree
        temp[r1][c2 + 1] -= degree
        temp[r2 + 1][c1] -= degree
        temp[r2 + 1][c2 + 1] += degree

    for y in range(len(temp) - 1):
        for x in range(len(temp[0] - 1)):
            temp[y][x + 1] += temp[y][x]

    for x in range(len(temp[0]) - 1):
        for y in range(len(temp) - 1):
            temp[y + 1][x] += temp[y][x]

    for y in range(len(board)):
        for x in range(len(board[y])):
            board[y][x] += temp[y][x]
            if board[y][x] > 0:
                answer += 1
