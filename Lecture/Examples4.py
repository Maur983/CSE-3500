#Extend for loop append.
import itertools
from collections import deque
def replace(s):
    for i in range(len(s)): #O(n) Time complexity
        if s[i]==" ":
            s[i]="_"
    return "".join(s)
#print(replace(["a"," ","b"," ","c"]))

def palindrome(s):
    be = 0
    end = len(s)-1
    while be<=end:
        if s[be]!=s[end]:
            return False
        be+=1
        end-=1
    return True
#print(palindrome("abcba"))

def sum_to_n(n):
    if n==1:
        return 1
    return n+sum_to_n(n-1) # What happens is 5 +sum_to_n(4), then 5+4+sum_to_n(3), then 5+4+3+sum_to_n(2) then lastly 5+4+3+2+1
#print(sum_to_n(5))

def fibonacci(n): #2^n because everytime we double the size and computation.
    if n==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
#for i in range(7):
    #print(fibonacci(i), end=", ")

def permutations_recur(nums): #Space O(n*n!) and Time is O(n!)
    if len(nums)==1:
        return nums
    result = []
    for i in range(len(nums)):
        current = nums[i]
        remaining = nums[:i]+nums[i+1]
        perms = permutations_recur(remaining)
        for p in perms:
            result.append(current+p)
    return result

def count_up(n):
    for i in range(n):
        print("About to Yield")
        yield i #Yield is good for memory as it only saves at a time.
        print("Out of Scope \n",)
#for x in count_up(5):
    #print(x)

def permutations_yi(nums):
    if len(nums) ==1:
        yield nums
        return
    for i in range(len(nums)):
        current = nums[i]
        remaining = nums[:i]+nums[i+1]
        perms = permutations_yi(remaining)
        for p in perms:
            yield [current]+p

def permutation(nums):
    result = [[]]
    for num in nums: #For each number
        new_result = []
        for perm in result:
            for i in range(len(perm)+1):
                new_perm = perm[:i]+ [num] +[perm[i:]]
                new_result.append(new_perm)
        result = new_result
    return result
nu = [1,2,3]
print(list(itertools.permutations(nu)))

def my_generator():
    yield "Hello world!!"
    yield "GeeksForGeeks"
#g = my_generator()
#print(next(g)) 
#print(next(g))

def product_sum(array, dept=1): #Time O(n) since we iterate over a list Space O(n) because in the worst scenario all of them are lists meaning we add more the function call stack
    total=0
    for i in array:
        if isinstance(i,list): #isinstance checks what variable it is and you extend it to check if it's something else.
            total += product_sum(i,dept+1)
        else:
            total+=i
    return total *dept