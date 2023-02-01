from collections import deque


def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])
    visited = [0 for _ in range(words)]

    while q:
        word, cnt = q.popleft()

        if word == target:
            return cnt

        for i in range(len(words)):
            if not visited[i]:
                if sum(y != x for y, x in zip(word, words)) == 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = 1

    return 0
