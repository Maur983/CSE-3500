#def search(values: list[int], target: int) -> bool:
    #for x in values:
        #if target == x:
            #return True
    #return False
#def add(a: int) -> int:
    #return a[0]+1
#def duplicates_in_list(mylist: list[int]) ->bool:
    #for i,x in enumerate(mylist):
        #for j,y in enumerate(mylist):
            #if x==i and i!=j:
                #return True
    #return False

def fizzbuzz(low,high):
    li=[]
    for x in range(low,high+1):
        if x %5 ==0 or x%7==0:
            li.append(x)
    print(", ".join(str(x) for x in li))
fizzbuzz(1,10)

def binary_naive(sort, target):
    for i,x in enumerate(sort):
        if x==target:
            return i
    return -1

def binary_advanced(sort, target):
    low =0
    high =len(sort)
    while low<=high:
        mid=(low+high)//2
        if sort(mid)==target:
            return mid
        elif sort(mid)<target:
            low=mid+1
        else:
            high=mid-1
    return -1

def problem(arr, sub):
    seq_i = 0
    for x in arr:
        if seq_i == len(sub):
            return True
        elif sub[seq_i] == x:
            seq_i+=1
    if seq_i == len(sub):
        return True
    else:
        False

def arr2(arr):
    new_arr = [0]*len(arr)
    left = 0
    right = len(arr)-1
    out_index = len(arr)
    while left<= right:
        if abs(abs[left])>abs(arr[right]):
            new_arr[out_index] = arr[left]**2
            left+=1
        else:
            new_arr[out_index] = arr[right]**2
            right=-1
        out_index-=1
    return new_arr


#def better_duplicates_in_list(belist: list[int]) ->bool:
    #for i,x in enumerate(belist):
        #for j,y in enumerate(belist):
            #if x==i and i!=j:
                #return True
    #return False

#def two_lists(list_one: list[int], list_two: list[int]) -> list[int]:
    #return list_one+list_two
def foo1(string):
    newstr = ""
    for i, x in enumerate(string):
        if i % 2 == 0:
            newstr = newstr+x.upper()
        else:
            newstr = newstr+x.lower()
    return newstr

assert foo1("Hello World") == "HeLlO WoRlD"

def foo2_flawed(arr1, arr2): #Time complexity O(n*m) Space is constant due to the pair list only being one
    smallest_value = float("inf")
    for i in arr1:
        for j in arr2:
            if smallest_value > abs(i-j):
                smallest_value = abs(i-j)
                pair = [i,j]
    return pair
def foo2_improved(arr1, arr2): #Time complexity O(n log(n)) Space Complexity O(1)
    arr1.sort()
    arr2.sort()
    smallest_value = float("inf")
    pair = []
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        x=arr1[i]
        y = arr2[j]
        diff = abs(x-y)
        if diff<smallest_value:
            smallest_value = diff
            pair = [x,y]
        if x<y:
            i+=1
        elif y<x:
            j+=1
        else:
            return pair

#if __name__ == "__main__":
    #search([x for x in range(100000)], 1000000)
