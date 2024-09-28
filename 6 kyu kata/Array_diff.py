def array_diff(a, b):
    res = []
    found = 0
    for i in a:
        for j in b:
            if i == j:
                found += 1
        if found == 0:
            res.append(i)
        else:
            found = 0
    return res
