def solution(progresses, speeds):
    answer = []

    for progress, speed in zip(progresses, speeds):
        left = -((progress - 100) // speed)
        if not answer or answer[-1][0] < left:
            answer.append([left, 1])
        else:
            answer[-1][1] += 1

    return [ans[1] for ans in answer]
