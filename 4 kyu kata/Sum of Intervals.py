def sum_of_intervals(intervals):
    
    intervals = sorted(list(set(intervals)))
    temp = list(intervals[0])
    not_overlapping_intervals = []  
    l = len(intervals)
    res = 0
    
    if l == 1:
        res = temp[1] - temp[0]
    else:  
        idx = 1
        while idx < l:
            if temp[0] <= intervals[idx][0] <= temp[1] and temp[1] <= intervals[idx][1]:
                temp[1] = intervals[idx][1]
            elif temp[0] <= intervals[idx][0] <= temp[1] and temp[1] > intervals[idx][1]:
                pass
            else:
                not_overlapping_intervals.append(temp)
                temp = list(intervals[idx])
                
            if idx + 1 == l:
                not_overlapping_intervals.append(temp)
                
            idx += 1
        
        for interval in not_overlapping_intervals:
            res += interval[1] - interval[0]
        
    return res
