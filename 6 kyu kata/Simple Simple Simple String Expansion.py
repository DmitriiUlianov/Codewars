def string_expansion(s):
    l = len(s)
    res = ''
    idx = 0
    while idx < l:
        if s[idx].isalpha():
            res += s[idx]
            idx += 1
        elif s[idx].isdigit():
            num = int(s[idx])
            idx += 1
            while idx < l and s[idx].isalpha():
                res += num*s[idx]
                idx += 1
    return res
