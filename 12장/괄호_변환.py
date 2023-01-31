def check(string):
    stack = []

    for bracket in string:
        if bracket == '(':
            stack.append('(')
        elif stack:
            stack.pop()
        else:
            return False

    return True


def dfs(string):
    if not string:
        return string
    close = 0

    for i in range(len(string)):
        if string[i] == '(':
            close += 1
        else:
            close -= 1

        if close == 0:
            if check(string[:i + 1]):
                return ''.join([string[:i + 1]], *dfs(string[i + 1:]))
            else:
                v = ['(', * dfs(string[i + 1:], ')')]
                for a in range(1, i):
                    if string[a] == '(':
                        v.append(')')
                    else:
                        v.append('(')
                return ''.join(v)


def solution(p):
    return dfs(p)
