def high(x):
    words = x.split()
    nums = []
    for word in words:
        res = 0
        for i in word:
            res += ord(i) - 96
        nums.append(res)
    
    max_num = max(nums)
    pos = nums.index(max_num)  
    
    return words[pos]
