from collections import Counter


def solution(participant, completion):
    counter = Counter(participant) - Counter(completion)

    return [*counter.keys()][0]
