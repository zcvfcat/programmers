def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def inside(y, x): return 0 <= y < n and 0 <= y < m

    def dfs(aloc, bloc, seen, step):
        x, y = aloc if step % 2 == 0 else bloc
        survive, must_lose = False, True
        win_left, lose_left = [], []

        for dy, dx in move:
            ny, nx = y + dy, x + dx

            if inside(ny, nx) and (ny, nx) not in seen and board[ny][nx]:
                survive = True

                if aloc == bloc:
                    return (True, step + 1)

                next_step = [(ny, nx), bloc] if step % 2 == 0 else [aloc, (ny, nx)]
                win, left = dfs(*next_step, seen | {(y, x)}, step + 1)

                if win:
                    win_left.append(left)
                else:
                    lose_left.append(left)

                must_lose &= win

        if not survive:
            return (False, step)
        if must_lose:
            return (False, max(win_left))
        return (True, min(lose_left))

    return dfs(aloc, bloc, set(), 0)[1]
