def multiply_digits(input_data=None):
    if input_data is None:
        return None
    
    digits = []

    if isinstance(input_data, (int, float)):
        num_str = str(input_data).replace('.', '')
        for char in num_str:
            if char.isdigit():
                digits.append(int(char))
                
    elif isinstance(input_data, str):
        for char in input_data:
            if char.isdigit():
                digits.append(int(char))
                
    elif isinstance(input_data, (list, tuple)):
        for item in input_data:
            if isinstance(item, (int, float)):
                num_str = str(item).replace('.', '')
                for char in num_str:
                    if char.isdigit():
                        digits.append(int(char))
    
    if not digits:
        return None
    
    result = 1
    for num in digits:
        result *= num
    
    return result
