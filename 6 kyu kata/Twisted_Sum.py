def compute_sum(n):
    total = 0
    while n > 0:
        if n < 10:
            total += n   
        else:
            nums = list(str(n))
            total += sum([int(i) for i in nums])
        n -= 1
    return total
