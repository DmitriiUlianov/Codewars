def make_sentences(parts):
    res = parts[0]
    for i in parts[1:]:  
        if i == ',':
            res += i
        elif i != '.':
            res += ' ' + i
    return res + '.'
