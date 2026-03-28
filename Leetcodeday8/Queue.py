class MyQueue(object):

    def __init__(self): #Time O(1) Space O(1)
        self.s1 = []
        self.s2 = []
        

    def push(self, x): #Time O(n) Space O(n)
        """
        :type x: int
        :rtype: None
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        

    def pop(self): #Time O(1) Space O(1)
        """
        :rtype: int
        """
        return self.s1.pop()
        

    def peek(self): #Time O(1) Space O(1)
        """
        :rtype: int
        """
        return self.s1[-1]
        

    def empty(self): #Time O(1) Space O(1)
        """
        :rtype: bool
        """
        return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()