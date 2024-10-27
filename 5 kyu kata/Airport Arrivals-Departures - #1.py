def flap_display(lines, rotors):
    
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'
    chars = list(string)
    len_chars = len(chars)
    
    res = [] 
    m = 0
    for line in lines:
        line = list(line)
        len_line = len(line)
        new_line = ''
        n = 0
        while n < len_line:
            st = ''
            for i in line:
                idx = chars.index(i)  
                new_idx = idx + rotors[m][n]
                while new_idx >= len_chars:
                    new_idx -= len_chars
                st += chars[new_idx]
        
            line = list(st)
            new_line += line[n]
            n += 1   
            
        res.append(new_line)
        m += 1 
           
    return res
