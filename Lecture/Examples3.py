from collections import deque
    
def foo(string): #Time O(n) cause not a nested loop Space O(n)
    stack = []
    for c in string:
        stack.append(c)
    print(stack)
    reversed_str =""
    while stack:
        reversed_str+=stack.pop()
    return reversed_str
print(foo("apple"))

def foo1(string):
    stack = []
    for c in string:
        stack.append(c)
    reversed_str = ""
    while stack:
        reversed_str +=stack.pop()
    return reversed_str

def foo2(string):
    stack = deque()
    for c in string:
        stack.append(c)
    reversed_str = ""
    while stack:
        reversed_str +=stack.pop()
    return reversed_str

def is_balancedlist(string): #Time O(n) Space O(n)
    stack = []
    pairs = {")","(","}","{","]","["} #keys are closing values and values are the opening
    open_chars = set(pairs.values)
    #if len(stack) == 0:
        #return True
    for c in string:
        if c in open_chars:
            stack.append(c)
        elif c in pairs: #Closing character
            if not stack:
                return False
        top  = stack.pop
        if top != pairs[c]:
            return False
    if len(stack) == 0:
        return True
    return len(stack) == 0

def best_digits(number, num_digits):
    stack = deque()
    for c in number:
        while (stack and num_digits>0 and stack[-1] < int(c) ):
            stack.pop()
            num_digits-=1
        stack.append(int(c))
    return "".join(str(x) for x in stack)
#print(best_digits("462839",2))

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class ListMapping:
    def __init__(self):
        self._entries =[]

    def put(self,key,value):
        e = self._entry(key)
        if e is not None:
            e.value = value
        else:
            self._entries.append(Entry(key,value))

    def _entry(self,key):
        for e in self._entries:
            if e.key ==key:
                return e
        return None
    
    def __setitem__(self, key, value):
        self.put(key,value)

    def get(self,key):
        e = self._entry(key)
        if e is not None:
            return e.value
        else:
            raise KeyError(str(key))
        
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        return self._entry(key) is not None
    
    def __iter__(self):
        for e in self._entries:
            yield e.key
    
    def values(self):
        for e in self._entries:
            yield e.value

    def items(self):
        for e in self._entries:
            yield(e.key, e.value)

class HashMapping:
    def __init__(self, size =8):
        self._size = size
        self._buckets = [ListMapping() for _ in range (size)]
        self._length = 0

    def _bucket(self,key):
        index = hash(key)%self._size
        return self._buckets[index]
    
    def put(self,key,value):
        bucket = self._bucket(key)
        if key not in bucket:
            self._length+=1
        bucket[key] = value
        if self._length>self._size:
            self._rehash()
    
    def __setitem__(self, key, value):
        self.put(key,value)

    
    def get(self,key):
        return self.get(key)
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __contains__(self,key):
        bucket = self._bucket(key)
        return key in bucket
    
    def __len__(self):
        for bucket in self._buckets:
            for key in bucket:
                yield key
    
    def values(self): #Loop through values
        for bucket in self._buckets:
            for val in bucket.values():
                yield val
    
    def items(self): #Loop through to get keys
        for bucket in self._buckets:
            for key, value in bucket.items():
                yield(key,value)

    def _rehash(self):
        old_items = list(self.items())
        self._size*=2
        self._buckets = [ListMapping for _ in range(self.size)]
        self._length = 0
        for key, value in old_items:
            self.put(key,value)

def func(string): #Time O(n) complexity Space complexity O(k) due to the the new variable.
    dic = {}
    for c in string:
        dic[c] = dic.get(c,0)+1

        #if c not in dic:
            #dic[c] = 1
        #else:
            #dic[c] =+1
    #return dic
#print(func("banana"))

def twosum(nums, target): #Time O(n) and Space O(n)
    #Or dic = dict()
    dic = {}
    needed = target - nums[i]
    for i in range(len(nums)):
        if nums[i] in dic:
            return [dic[needed], i]
    dic[nums[i]] = i

def print_ab(a,b):
    nums = []
    for i in range(a,b+1):
        if i%7==0 or i%5==0:
            nums.append(str(i))
    print(', '.join(nums))
print_ab(1,10)

class Product:
    def __init__(self, good_quality=True):
        self.good_quality = good_quality
def pro(lispro):
    low = 0
    high = len(lispro)-1
    while(high>low):
        mid = (high+low)//2
        if lispro[mid].good_quality is True:
            low = mid+1
        else:
            high = mid
    return low
#pro1 = Product()
#pro2 = Product()
#pro3 = Product(False)
#pro4 = Product(False)
#li = [pro1,pro2,pro3,pro4]
#print(pro(li))

def move(array, to_move):#log(n)
    left =0
    right = len(array)-1
    while left<right:
        if array[right]==to_move:
            right -=1
        elif array[left]==to_move:
            array[left], array[right] = array[right], array[left]
        else:
            left+=1
    return array
#print(move([1,2,2,4,3],2))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def pointer(head, k):
    fast = head
    slow = head
    #move fast k steps ahead
    for _ in range(k):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next