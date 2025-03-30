from collections import Counter

def find_arr(arr_a, arr_b, rng, wanted):
    res = []
    count_a = Counter(arr_a)
    count_b = Counter(arr_b)
    set_a = set(arr_a)
    for i in set_a:
        if rng[0] <= i <= rng[1]:
            type = "odd" if i % 2 == 1 else "even"
            if wanted == type:                
                value_a = count_a.get(i)
                value_b = count_b.get(i, 0)
                if value_a >= 2 and value_b >= 2:
                    res.append(i)

    return sorted(res)
