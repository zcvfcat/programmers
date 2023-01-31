def combinations(array, tie):
    ans = [array]

    if tie == 0:
        return [ans]

    for idx, node in enumerate(array):
        for edges in combinations(array[idx + 1:], tie - 1):
            ans += [(node, *edges)]

    return ans


def solution(numbers):
    answer = set()
    selects = list(combinations(numbers, 2))

    for select in selects:
        (a, b) = select
        answer.add(a + b)

    return sorted(answer)
