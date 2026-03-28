class LRUCache:

    def __init__(self, capacity): #Time O(1) Space O(1)
        self.dict = dict()
        self.capacity = capacity
        

    def get(self, key): #Time O(1) Space O(1)
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)
        self.dict[key] = val   
        return val        
        

    def put(self, key, value): #Time O(1) Space O(1)
        if key in self.dict:    
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]         
        self.dict[key] = value