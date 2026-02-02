from functools import wraps
def simple_cache(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args,tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper