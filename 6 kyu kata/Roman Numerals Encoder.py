def solution(n):
    roman = ""
    if n >= 1000:
        nums = [int(i) for i in str(n)]
        roman += "M" * nums[0]
        n -= 1000 * nums[0]
    if n >= 900:
        roman += "CM"
        n -= 900
    if n >= 500:
        roman += "D"
        n -= 500
    if n >= 400:
        roman += "CD"
        n -= 400
    if n >= 100:
        nums = [int(i) for i in str(n)]
        roman += "C" * nums[0]
        n -= 100 * nums[0]
    if n >= 90:
        roman += "XC"
        n -= 90
    if n >= 50:
        roman += "L"
        n -= 50  
    if n >= 40:
        roman += "XL"
        n -= 40
    if n >= 10:
        nums = [int(i) for i in str(n)]
        roman += "X" * nums[0]
        n -= 10 * nums[0]
    if n == 9:
        roman += "IX"
        n -= 9
    if n >= 5:
        roman += "V"
        n -= 5 
    if n >= 4:
        roman += "IV"
        n -= 4
    if n >= 1:
        roman += "I" * n
    
    return roman
