def cache_decorator(max_size=100):
    def cache_decorator_inner(func):
        cache = {}
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in cache:
                val = cache.pop(key)
                cache[key] = val
                return val
            val = func(*args, **kwargs)
            if len(cache)>= max_size:
                oldest_key = next(iter(cache))
                del cache[oldest_key]
            cache[key] = val
            return val
        return wrapper
    return cache_decorator_inner

@cache_decorator(100)
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)