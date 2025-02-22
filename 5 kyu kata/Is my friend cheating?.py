# a*b = s - (a + b)
# a*b + a + b = s
# a*b + a + b + 1 = s + 1
# (a + 1)*(b + 1) = s + 1 
# s + 1 is a product of (a + 1) and (b + 1)

def remov_nb(n):
    s = n*(n + 1)//2  # Sum of range(1,n + 1)
    res = []

    for a in range(1, n + 1):
        b = (s + 1)/(a + 1) - 1
        if b.is_integer() and 1 <= b <= n:
            res.append((a, int(b)))

    return res
