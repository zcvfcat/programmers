from heapq import heappush, heappop  # 책 나오면 보자...


def push_task(waiting, tasks):
    start, priority, end = heappop(tasks)
    heappush(waiting, (priority, start, end))
    return start


def solution(program):
    answer = [0 for _ in range(11)]
    tasks, waiting, curr = [], [], 0

    for p in program:
        # p[1]이 시작시간, p[0] 우선순위, p[2] 종료시간
        heappush(tasks, (p[1], p[0], p[2]))

    while tasks or waiting:
        if not waiting:
            curr = push_task(waiting, tasks)

        priority, start, end = heappop(waiting)
        answer[priority] += curr - start
        curr += end

        while tasks and tasks[0][0] <= curr:
            push_task(waiting, tasks)

    answer[0] = curr
    return answer
