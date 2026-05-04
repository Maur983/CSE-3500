from functools import lru_cache
import time
#start = time.perf_counter()
#end = time.perf_counter()
#total = end -start
@lru_cache(maxsize=None)
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

def outer():
    print("Hello from outer")
    def inner():
        print("Hello from inner")
    return inner()

def my_decorator(func):
    def wrapper():
        print("Before func")
        func()
        print("After func")
    return wrapper

def decorator_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print("Before func")
        rv = func(*args, **kwargs)
        end = time.perf_counter()
        print(end-start)
        print("After func")
        return rv
    return wrapper

@decorator_time
def func_a(x,y):
    return x+y

@my_decorator
def func_b():
    print("In func_b")

@my_decorator
def add(x,y):
    return x+y
#or new_add = my_decorator(add)
#wrapped_a = my_decorator(func_a)
#wrapped_a()
#wrapped_b = my_decorator(func_b)
#wrapped_b()
#print(func_a(1,2))
#func_b()
def decorator_factory(parameter):
    def decorator(func):
        def wrapper(*args, **kwarags):
            rv = func(args, kwarags)
            return rv
        return wrapper
    return decorator

def cache_decorator(max_size =128): #Issue with this is how their is no limit meaning it can take up a lot of memory so we needed did this
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

class Student:
    def __init__(self,name, gpa, netid):
        self.name = name
        self.gpa = gpa
        self.netid = netid
class CSE3500Student(Student):
    def __init__(self, homework_grade,*args, **kwargs):
        self.homework_grade = homework_grade
        super().__init__(*args,**kwargs)

@cache_decorator()
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

def lcs_len(x,y,i,j): #Time(2^(n+m)) Space(n+m) with the cache its Time is O(n*m) and Space O(n*m) we nred to customize the cache as lists are not hashable
    if i ==0 or j==0:
        return 0
    if x[i-1] == y[j-1]:
        return 1+ lcs_len(x,y,i-1,j-1)
    return max(lcs_len(x,y,i-1,j), lcs_len(x,y,i,j-1))

def lcs_memo(x,y,i,j, cache=None): #Top Down
    if cache is None:
        cache = {}
    if (i,j) in cache:
        return [(i,j)]
    if i<=0 or j<=0:
        return 0
    if x[i-1] == y[j-1]:
        cache[(i,j)] = 1+lcs_memo(x,y,i-1,j-1,cache)
    else:
        cache[(i,j)] = max(lcs_memo(x,y,i-1,j), lcs_memo(x,y,i,j-1))
        return cache[(i,j)]
    
def lcs_bottom_up(x,y): #Time O(n*m) Space O(n*m) Bottom up
    m=len(x)
    n=len(y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def recover_subsequence(x,y,dp):
    i=len(x)
    j=len(y)
    chars = []
    while i>0 and j>0:
        if x[i-1] == y[j-1]:
            chars.append(x[i-1])
            i-=1
            j-=1
        elif dp[i-1][j]>=dp[i][j-1]:
            i=-1
        else:
            j=-1
    chars.reverse()
    return ''.join(chars)

def max_subarray(nums): #Brute force Time O(n^2) Space O(1)
    best = float('-inf')
    for i in range(len(nums)-1):
        current_sum =0
        for j in range(i, len(nums)-1):
            current_sum +=nums[j]
            best = max(best,current_sum)
    return best

def max_subarray_kadanes(nums): #Time O(n) and Space O(1)
    current = nums[0]
    best = nums[0]
    for x in nums[1:]:
        current = max(x, x+current)
        best = max(best, best+current)
    return best

def max_subarray_dp (nums):
    dp =[0]*len( nums)
    dp [0] = nums [0]
    for i in range (1 ,len(nums)) :
        dp[i] = max(nums[i], nums [i]+dp[i-1])
    return max (dp)