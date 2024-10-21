def match(net_addr: str, wc_mask: str, ipv4_addr: str) -> bool:
    
    def func(string):
        string = [bin(int(i))[2:] for i in string.split('.')]
        res = ''
        for i in string:
            res += '.' + '0'*(8 - len(i)) + i 
        return res[1:]
    
    net_addr = func(net_addr)
    wc_mask = func(wc_mask)
    ipv4_addr = func(ipv4_addr)
    
    j = 0
    for i in wc_mask:
        if i == '0' and net_addr[j] != ipv4_addr[j]:
            return False
        j += 1
        
    return True
