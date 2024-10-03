def ips_between(start, end):

    start = [int(i) for i in start.split('.')]
    end = [int(i) for i in end.split('.')]
        
    def func(mylist):
        total = 0
        k = 3
        for i in mylist:
            total += i*256**k
            k -= 1
        return(total)
        
    return func(end) - func(start)
