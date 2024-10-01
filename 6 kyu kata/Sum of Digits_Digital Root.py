def digital_root(n):
    while n > 9:
        string = list(str(n))
        n = sum([int(i) for i in string])
    return n
