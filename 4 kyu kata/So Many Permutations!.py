from itertools import permutations as perm
def permutations(s):
    res = set(perm(s))
    return ["".join(i) for i in res]
    
