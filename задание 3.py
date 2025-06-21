def max_odd(array):
    max_odd_value = None
    
    for item in array:
        
        if isinstance(item, (int, float)):
            
            num = int(item) if isinstance(item, float) and item.is_integer() else item
            
            
            if isinstance(num, int) and num % 2 != 0:
                if max_odd_value is None or num > max_odd_value:
                    max_odd_value = num
    
    return max_odd_value