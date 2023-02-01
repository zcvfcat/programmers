def radix_change(num, radix):
    if num == 0:
        return '0'
    nums = []

    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return ''.join(reversed(nums))


def solution(n):
    return int(radix_change(n, 3)[:: -1], 3)
