import sys
sys.setrecursionlimit(10 ** 6)


def fibo(n, answer):
    if n < 2:
        return 1

    if answer[n] == 0:
        answer[n] = fibo(n - 1, answer) + fibo(n - 2, answer)

    return answer[n]


def solution(n):
    answer = [0 for _ in range(n)]
    answer[0] = answer[1] = 1
    fibo(n - 1, answer)

    return answer[-1] % 1234567
