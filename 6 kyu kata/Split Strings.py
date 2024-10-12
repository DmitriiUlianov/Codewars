def solution(s):
    length = len(s)
    rem = length % 2
    l = []
    n = 0

    while n < length - 1:
        l.append(s[n : n + 2])
        n += 2
    if rem != 0:
        l.append(s[length - 1] + "_")
    return l
