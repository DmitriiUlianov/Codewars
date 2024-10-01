def rgb(r, g, b):
    
    def func(x):
        if x < 0:
            x = 0
        elif x > 255:
            x = 255
        x = hex(x)[2:].upper()
        x = x if len(x) == 2 else '0' + x
        return x
        
    rgblist = [r, g, b]
    res = ''
    for i in rgblist:
        res += func(i)   
    return res
