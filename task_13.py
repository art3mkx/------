import time
from collections import OrderedDict
from functools import wraps

def cached(max_size=None, seconds=None):
    try:
        max_size = int(max_size) if max_size is not None else None
    except (TypeError, ValueError):
        max_size = None
    
    try:
        seconds = int(seconds) if seconds is not None else None
    except (TypeError, ValueError):
        seconds = None
    
    def decorator(func):
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            
            if key in cache:
                cached_time, result = cache[key]
                
                if seconds is None or (time.time() - cached_time) < seconds:
                    cache.move_to_end(key)
                    return result
            result = func(*args, **kwargs)
            cache[key] = (time.time(), result)
            if max_size is not None and len(cache) > max_size:
                cache.popitem(last=False)
            
            return result
        
        return wrapper
    
    return decorator