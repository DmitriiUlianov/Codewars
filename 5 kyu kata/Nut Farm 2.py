def shake_tree(tree):
    l = len(tree[0])
    res = [0]*l
    for n, row in enumerate(tree):   
        for m, smth in enumerate(row):
            if smth == 'o':
                stuck = 0
                for level in tree[(n + 1):]: 
                    if level[m] == '\\':    
                        while m + 1 < l:
                            if level[m + 1] == '/':
                                stuck = 1
                                break
                            elif level[m + 1] == '\\':
                                m += 1
                            else:
                                m += 1
                                break
                    
                    elif level[m] == '/':
                        while m - 1 >= 0:
                            if level[m - 1] == '\\':
                                stuck = 1
                                break
                            elif level[m - 1] == '/':
                                m -= 1
                            else:
                                m -= 1
                                break
                            
                    if stuck == 1:
                        break
                        
                if stuck == 0:
                    res[m] += 1
    return res
