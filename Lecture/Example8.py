import heapq
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors: tuple[Node, int] = []

    def add_edge(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))
    
    def __repr__(self):
        return f"Node({self.value})"

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self,value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
    
    def add_edge(self, from_value, to_value, weight):
        if from_value not in self.nodes:
            self.add_node(from_value)
        if to_value not in self.nodes:
            self.add_node(to_value)
        self.nodes[from_value].add_edge(self.nodes[to_value], weight)
    
    def get_node(self, value):
        return self.nodes.get(value)

def dijstra(graph, start): #Time (O(V+E)logv) Space O(V)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0,start)]
    while pq:
        curr_dist , node=heapq.heappop(pq)
        #Prevent Cycles
        if curr_dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = curr_dist+weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

#Goal is to choose the interval that will not overrlap 
def interval_scheduling(intervals): #Time O(nlogn) Space O(1)
    intervals.sort(key = lambda x: x[1]) #This means sort by the end times lambda is a function key = will indicate what to sort by in this its the other integer in the tuple
    count = 0
    current_end = float('-inf')
    for start,end in intervals: #You could also do i instead start and end and set start = i[0] end = i[1] cleanly start, end = interval
        if start >= current_end:
            count+=1
            current_end = end
    return count
#print(interval_scheduling([(2,2),(1,3),(3,8),(2,4)]))
#Another way
def get_end_time(interval):
    start , end = interval
    # Or return interval [1]
    return end
#get_end_time = lambda x :x[1]
#or = .sort(key= lambda x :x[1])
def inter(intervals):
    intervals.sort(key = get_end_time)
    count = 0
    current_end = float('-inf')
    for interval in intervals:
        start = interval[0]
        end = interval[1]
        if start <= current_end:
            count+=1
            current_end = end
    return count

def prim(graph, start): #Time O((V+E)log(v)) , Space O(V)
    visited = set([start])
    edges = []
    total = 0
    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight ,start , neighbor))
    while edges:
        weight, _, curr_neighbor = heapq.heappop(edges)
        if curr_neighbor not in visited:
            visited.add(curr_neighbor)
            total +=weight
            for neighbor , weight in graph[curr_neighbor]:
                if neighbor not in visited:
                    heapq.heappush(edges, (weight ,curr_neighbor, neighbor))
    return total

def kruskal(vertices, edges): #Time O(ElogE) Space O(E) due to the recursion through the edges
    parent = {v: v for v in vertices}
    def find(x): #This is a closure capturing this parent value this is used for multiple parameters like if you multiple parameters but only one changes you would not bother putting them in the arguments
        if parent[x] !=x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        parent[find(x)] = find(y)
    edges.sort(key = lambda x: x[2])
    mst_weight = 0
    for u,v,weight in edges:
        #If we have no cycle
        if find(u) != find(v):
            union(u,v)
            mst_weight+=weight
    return mst_weight

class Node :
    def __init__ (self,freq,char=None,left=None,right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    
    def __lt__(self,other):
        if isinstance(other,Node):
            return self.freq < other.freq
        return NotImplemented

def huffman(frequencies): #Time O(nlogn) Space O(n)
    heap = [Node(freq,char) for char , freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        merged = Node(n1.freq+n2.freq,None,n1,n2)
        heapq.heappush(heap,merged)
    return heap[0]

def fibbonacci(n): #Easy to write but very inefficient as it's O(2^n) Space is O(n) with one stack at a time
    if n<=1:
        return n
    return fibbonacci(n-1)+fibbonacci(n-2)
#print(fibbonacci(5))

def fib_memo_he(n, cache=None):
    cache = {0:0,1:1}
    fib_help(n, cache)

def fib_help(n , cache):
    if n in cache:
        return cache[n]
    if n<=1:
        return n
    #Compute and store in cache
    cache[n] = fib_memo(n-1, cache)+ fib_memo(n-2, cache)
    return cache[n]

def fib_memo(n , cache=None): #Time O(n) Space O(n)
    if cache is None:
        cache = {0:0,1:1}
    if n in cache:
        return cache[n]
    #Compute and store in cache
    cache[n] = fib_memo(n-1, cache)+ fib_memo(n-2, cache)
    return cache[n]
print(fib_memo(5))


#Closures
#mylist = [1,2,3]
#def foo():
    #print(mylist)
#foo()
#stuff = [1,2,3,4] make it into a tuple then convert to list in the function if you want a default.
#def foo2(stuff= stuff): #Don't do this it will be mutable so when you update it in the function the default will change
    #print(stuff)
#foo2()