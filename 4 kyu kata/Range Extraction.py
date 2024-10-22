def solution(args):
    res = str(args[0])
    l = len(args)
    n = 1
    count = 0
    for i in args[1:]:
        if args[n - 1] + 1 == args[n]:
            count += 1
            if n == l - 1:
                if count == 1:
                    res += ',' + str(args[n])
                else:
                    res += '-' + str(args[n])
        else:
            if count == 0:
                res += ',' + str(args[n])     
            elif count == 1:
                res += ',' + str(args[n - 1])
                res += ',' + str(args[n])
                count = 0
            elif count > 1:
                res += '-' + str(args[n - 1])
                res += ',' + str(args[n])
                count = 0
        n += 1
                       
    return res
