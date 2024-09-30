def format_duration(sec):
    
    min = sec // 60
    hours = min // 60 
    days = hours // 24
    years = days // 365
    
    days = days % 365
    hours = hours % 24
    min = min % 60
    sec = sec % 60
    
    dur = []
    if years > 0:
        dur.append('1 year') if years == 1 else dur.append(str(years) + ' years')
    if days > 0:
        dur.append('1 day') if days == 1 else dur.append(str(days) + ' days')
    if hours > 0:
        dur.append('1 hour') if hours == 1 else dur.append(str(hours) + ' hours')
    if min > 0:
        dur.append('1 minute') if min == 1 else dur.append(str(min) + ' minutes')
    if sec > 0:
        dur.append('1 second') if sec == 1 else dur.append(str(sec) + ' seconds')
        
    l = len(dur)
    if l == 0:
        return 'now'
    res = ', '.join(dur[0:l-1])
    res += ' and ' + dur[l-1]  
    return res if l > 1 else dur[0]
