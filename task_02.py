def coincidence(lst=None, rng=None):
    if lst is None or rng is None:
        return []
    
    result = []
    start = rng.start
    stop = rng.stop
    step = rng.step if rng.step is not None else 1
    
    for item in lst:
        if isinstance(item, (int, float)):
            if start <= item < stop:
                if abs((item - start) % step) < 1e-10:
                    result.append(item)
    
    return result
