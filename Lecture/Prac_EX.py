class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left= left
        self.right = right


def bst_recur(node,target): #Time (nlogn) Space O(n)
    if node.value == target:
        return True
    elif node.value>target:
        return bst_recur(node.left, target)
    else:
        return bst_recur(node.right, target)

def bst(node,target): #Time (nlogn) Space O(1)
    while node:
        if node.value == target:
            return True
        elif node.value>target:
            return bst(node.left, target)
        else:
            return bst(node.right, target)
    return False
    
nod = Node(3)
nod1 = Node(2)
nod2 = Node(1)
nod3 = Node(4)
nod.left = nod2
nod.right = nod1
nod1.right = nod3
#print(bst(nod, 1))

def foo(intervals): # This greedy algorithim interval scheduling # Time O(nlogn) Space is O(1) thid works for lists within lists
    #lambda x : x[1] means this will sort by the second values
    intervals.sort(key=lambda x :x[1])
    count = 0
    current_end = float('-inf')
    for s,e in intervals:
    #can do for  i in interval: s,e=interval
        if s >= current_end:
            count+=1
            current_end = e
    return count
#print(foo([[1,2],[3,4],[5,7]]))

def coin_change(coins, amount): #Time O(nlogn) Space O(1)
    coins.sort(reverse=True)
    count = 0
    for co in coins:
        if co ==amount:
            amount-=co
            count+=1
            return count
        while co<=amount:
            amount-=co
            count+=1
    return count
#print(coin_change([1,5,10,25],25))

def dya_coins(coins,amount): #Time O(A+C) Space O(n)
    count =0
    dp = [float('inf')]*(amount+1)
    dp[0] =0
    for a in range(1, amount+1):
        for coin in coins:
            if coin<=a:
                dp[a]=min(dp[a], dp[a-coin]+1)
    if dp[amount]!=float('inf'):
        return dp[amount]
    else:
        return -1
print(dya_coins([25,10,5,1],7))


def fib(n): #Time O(n) Space O(n)
    return fib_helper(n, cache={})
def fib_helper(n, cache):
    if n in cache:
        return cache[n]
    else:
        if n <=1:
            val = n
        else:
            val = fib_helper(n-1, cache) + fib_helper(n-2, cache)
            cache[n] = val
        return val