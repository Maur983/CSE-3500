class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val): #Time O(1) Space O(1)
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.min)==0:
            self.min.append(val)
        elif self.min[-1]<val:
           self.min.append(self.min[-1])
        else:
            self.min.append(val)

    def pop(self): #Time O(1) Space O(1)
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()
        

    def top(self): #Time O(1) Space O(1)
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self): #Time O(1) Space O(1)
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()