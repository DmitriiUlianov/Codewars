def variance(numbers): 
    l = len(numbers)
    mean = sum(numbers)/l
    variance = [(i - mean)**2 for i in numbers]
    res = sum(variance)/l
    return res
