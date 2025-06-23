def connect_dicts(dict1, dict2):
    
    sum1 = sum(v for v in dict1.values() if isinstance(v, (int, float)))
    sum2 = sum(v for v in dict2.values() if isinstance(v, (int, float)))
    priority_dict = dict2 if sum2 >= sum1 else dict1
    secondary_dict = dict1 if priority_dict is dict2 else dict2

    result = {}

    for key, value in priority_dict.items():
        if isinstance(value, (int, float)) and value >= 10:
            result[key] = value

    for key, value in secondary_dict.items():
        if isinstance(value, (int, float)) and value >= 10 and key not in result:
            result[key] = value

    return dict(sorted(result.items(), key=lambda item: item[1]))
