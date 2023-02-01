def solution(word):
    preset = {
        'A': [1, 1, 1, 1, 1],
        'E': [782, 157, 32, 7, 2],
        'I': [1563, 313, 63, 13, 3],
        'O': [2344, 469, 94, 19, 4],
        'U': [3125, 625, 125, 25, 5]
    }

    answer = 0
    for idx, key in enumerate(word):
        answer += preset[key][idx]

    return answer
