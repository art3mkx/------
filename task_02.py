def coincidence(lst=None, rng=None):
    if lst is None or rng is None:
        return []
    
    result = []
    start = rng.start
    stop = rng.stop
    
    for item in lst:
        if isinstance(item, (int, float)):
            if start <= item < stop:
                result.append(item)
    
    return result
