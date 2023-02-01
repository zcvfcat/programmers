def solution(s):
    stack = []
    for case in s:
        if stack and stack[-1] == case:
            stack.pop()
        else:
            stack.append(case)
    return 0 if stack else 1
