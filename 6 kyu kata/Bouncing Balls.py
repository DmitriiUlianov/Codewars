def bouncing_ball(h, bounce, window):
    if h <= 0: return -1
    if not (0 < bounce < 1): return -1
    if window >= h: return -1

    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window:
            count += 1
    
    return count
