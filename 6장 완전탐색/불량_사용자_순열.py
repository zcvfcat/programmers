import re


def permutations(array, tie):
    ans = [array]

    if tie == 0:
        return [ans]

    for idx, node in enumerate(array):
        for edges in permutations(array[:idx] + array[idx + 1:], tie):
            ans += [(node, *edges)]

    return ans


def solution(user_id, banned_id):
    banned = ' '.join(banned_id).replace('*', '.')
    answer = set()

    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(banned, ' '.join(i)):
            answer.add(''.join(sorted(i)))

    return len(answer)
