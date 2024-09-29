def make_readable(sec):
    
    min = sec // 60
    sec = sec % 60
    hours = min // 60 
    min = min % 60
    
    hours = str(hours) if hours > 9 else '0' + str(hours)
    min = str(min) if min > 9 else '0' + str(min)
    sec = str(sec) if sec > 9 else '0' + str(sec)
    
    return hours + ':' + min + ':' + sec
