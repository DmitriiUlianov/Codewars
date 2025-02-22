def hist(s):
    errors = []
    for i in s:
        if i == 'u' or i == 'w' or i == 'x' or i == 'z':
            errors.append(i)
    errors.sort()
    error = ''.join(errors) + '.'

    res = ''
    count = 0
    j = error[0]
    for i in error:
        if j == i:
            count += 1
        else: 
            c = str(count)
            res += j + '  ' + c + (6 - len(c))*' ' + count*'*' + '\r'
            j = i
            count = 1
                 
    end = len(res) - 1
    return res[:end]
