def fibbonacci(n,cache=None): #Time O(n) because it goes from the range of n to the last number and the Space is O(n) as it saves the data into the dictionary.
    if cache is None:
        cache = {0:0,1:1}
    if n in cache:
        return n
    cache[n] = fibbonacci(n-1, cache) +fibbonacci(n-2, cache)
    return cache[n]