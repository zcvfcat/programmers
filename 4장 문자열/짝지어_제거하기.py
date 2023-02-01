# 실패하는게 정상이라고 함
def solution(s):
    while len(s) > 1:
        s = list(s)

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s[i] = s[i + 1] = ''

        new_s = ''.join(s)
        if len(s) == len(new_s):
            break
        s = new_s

    return 1 if len(s) == 0 else 0
