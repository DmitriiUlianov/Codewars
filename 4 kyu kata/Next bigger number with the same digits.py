'''Algorithm:
Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit. 
For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then output is “Not Possible”.
Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. For “534976″, the right side of 4 contains “976”. 
The smallest digit greater than 4 is 6.
Swap the above found two digits, we get 536974 in above example.
Now reverse all digits from position next to ‘d’ to the end of number to get the result. For above example, we reverse the digits in bold 536974. 
We get “536479” which is the next greater number for input 534976..
'''
def next_bigger(n):
    
    nums = [int(i) for i in str(n)]
    l = len(nums)
    if l == 1:
        return -1
    
    x = 0
    while l - 2 >= 0:
        if nums[l - 2] < nums[l - 1]:
            x = nums[l - 2]
            idx_x = l - 2
            break
        elif l - 2 == 0 and x == 0:
            return -1
        l -= 1
    
    l = len(nums)
    y = nums[idx_x + 1]
    idx_y = idx_x + 1
    k = idx_y
    while k < l - 1:
        if nums[k + 1] <= y and nums[k + 1] > x:
            y = nums[k + 1]
            idx_y = k + 1
        k += 1
        
    nums[idx_x], nums[idx_y] = nums[idx_y], nums[idx_x]
    part1 = nums[:idx_x + 1]
    part2 = nums[idx_x + 1:]
    res = part1 + part2[::-1]
    res = [str(i) for i in res]
    return int(''.join(res))
  
