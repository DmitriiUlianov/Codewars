def ipv4_to_binary(ipv4_addr: str) -> str:
    ipv4 = [bin(int(i))[2:] for i in ipv4_addr.split('.')]
    res = ''
    for i in ipv4:
        res += '.' + '0'*(8 - len(i)) + i   
    return res[1:]
