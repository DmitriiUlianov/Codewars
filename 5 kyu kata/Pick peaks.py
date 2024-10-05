def pick_peaks(arr):
    pos = []
    peaks = [] 
    res = {"pos":pos, "peaks":peaks}
    l = len(arr)
    if l == 0:
        return res  
        
    idx = 1           
    while idx < l - 1:
        if arr[idx - 1] < arr[idx] and arr[idx] > arr[idx + 1]:
            peaks.append(arr[idx])
            pos.append(idx)
        elif arr[idx - 1] < arr[idx] and arr[idx] == arr[idx + 1]:
            peak_idx = idx
            while idx < l - 1:
                if arr[idx] != arr[idx + 1]:
                    if arr[idx] > arr[idx + 1]:
                        peaks.append(arr[idx])
                        pos.append(peak_idx)
                    break
                idx += 1
        idx += 1
    return res
