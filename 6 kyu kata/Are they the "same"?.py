def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    
    array1 = [i*i for i in array1]
    
    return True if sorted(array1) == sorted(array2) else False
