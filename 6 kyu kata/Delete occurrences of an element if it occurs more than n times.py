def delete_nth(order,max_e):
    dict = {}
    res = []
    for i in order:
        if i not in dict:
            res.append(i)
            dict[i] = 1
        elif dict[i] < max_e:
            res.append(i)
            dict[i] += 1
    return res
