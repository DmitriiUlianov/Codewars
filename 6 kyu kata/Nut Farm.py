def shake_tree(tree):
    l = len(tree[0])
    res = [0]*l
    for idx, smth in enumerate(tree[0]):
        if smth == 'o':
            stuck = 0
            for level in tree[1:]: 
                if level[idx] == '\\':
                    idx += 1
                elif level[idx] == '/':
                    idx -= 1
                elif level[idx] == '_':
                    stuck = 1
                    break
            if stuck == 0:
                res[idx] += 1

    return res
