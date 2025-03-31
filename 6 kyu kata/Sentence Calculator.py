def letters_to_numbers(s):
    res = 0
    for i in s:
        num = ord(i)
        if 48 <= num <= 57:
            res += (num - 48)
        elif 97 <= num <= 122:
            res += (num - 96)
        elif 65 <= num <= 90:
            res += 2*(num - 64)
    return res
        
