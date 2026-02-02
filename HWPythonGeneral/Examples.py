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
    
    return True


#def better_duplicates_in_list(belist: list[int]) ->bool:
    #for i,x in enumerate(belist):
        #for j,y in enumerate(belist):
            #if x==i and i!=j:
                #return True
    #return False

#def two_lists(list_one: list[int], list_two: list[int]) -> list[int]:
    #return list_one+list_two
def foo(string):
    newstr = ""
    for i, x in enumerate(string):
        if i % 2 == 0:
            newstr += x.upper()
        else:
            newstr += x.lower()
    return newstr

assert foo("Hello World") == "HeLlO WoRldD"

#if __name__ == "__main__":
    #search([x for x in range(100000)], 1000000)
