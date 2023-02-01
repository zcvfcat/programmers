from heapq import heapify, heappush, heappop  # 링크 없음..


def solution(ability, number):
    heapify(ability)

    for _ in range(number):
        a, b = heappop(ability), heappop(ability)

        heappush(ability, a + b)
        heappush(ability, a + b)

    return sum(ability)
