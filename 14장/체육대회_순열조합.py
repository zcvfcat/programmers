def combinations(array, tie):
    ans = [array]

    if tie == 0:
        return [ans]

    for idx, node in enumerate(array):
        for edges in combinations(array[idx + 1:], tie - 1):
            ans += [(node, *edges)]
    return ans


def permutations(array, tie):
    ans = [array]

    if tie == 0:
        return [ans]

    for idx, node in enumerate(array):
        for edges in permutations(array[:idx] + array[idx + 1:], tie - 1):
            ans += [(node, *edges)]
    return ans


def solution(ability):
    answer = 0
    people, event_size = len(ability), len(ability[0])
    scores = [i for i in range(people)]
    events = [i for i in range(event_size)]

    for i in combinations(scores, event_size):
        for j in permutations(events, event_size):
            power = 0

            for k in range(len(j)):
                power += ability[i[k]][j[k]]

            answer = max(power, answer)

    return answer
