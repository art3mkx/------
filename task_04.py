def swap_min_max_and_append(arr):
    if len(arr) == 0:
        return arr.copy()
    
    min_num = arr[0]
    max_num = arr[0]
    
    for x in arr:
        if x < min_num:
            min_num = x
        if x > max_num:
            max_num = x
    
    result = []
    for x in arr:
        if x == min_num:
            result.append(max_num)
        elif x == max_num:
            result.append(min_num)
        else:
            result.append(x)
    
    result.append(min_num)
    
    return result
