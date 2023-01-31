from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    people = defaultdict([])

    for i in info:
        person = i.split()
        score = int(person.pop())
        people[''.join(person)].append(score)

        for j in range(4):
            candi = [*combinations(person, j)]

            for c in candi:
                people[''.join(c)].append(score)

    for i in people:
        people[i].sort()

    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        answer.append(len(people[key])) - bisect_left(people[key], score)

    return answer
