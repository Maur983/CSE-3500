class Node:
    def __init__(self,value, next=None, prev=None): #Time O(1) Space O(1) intialization
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self): #Time O(1) Space O(1) intialization
        self.head = None
        self.tail = None
        self.length =0
    
    def size(self): #Time O(1) Space O(1)
        return self.length
    
    def prepend(self ,value): #Time O(1) adding one element at the begining Space O(1)
        new_node = Node(value)
        old_head = self.head
        new_node.next = self.head
        self.head = new_node
        old_head.prev = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
    
    def append(self,value): #Time O(1) adding one element at the end Space O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def insert_at(self,index,value): #Time O(n) loop through the list in worst case and Space O(1)
        if index < 0 or index > self.length :
            return
        if index == 0:
            self.prepend(value)
            return
        if index == self.length :
            self.append(value)
            return
        new_node = Node(value)
        current = self.head
        for i in range(index-1):
            current = current.next
        nex = current.next
        new_node.prev = current
        current.next = new_node
        nex.prev = new_node
        new_node.next = nex
    
    def remove_at(self,index): #Time O(n) loop through the list in worst case and Space O(1)
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
                return
        current = self.head
        for i in range(index-1):
            current = current.next
        if current.next == self.tail:
            self.tail = current
        else:
            removed = current.next
            new_next = removed.next
            new_next.prev = current
            current.next = new_next
        self.length-=1
        return removed.value
    
    def is_empty(self): #Time O(1) Space O(1)
        if self.length ==0:
            return True
        else:
            return False

    def get(self, index): #Time O(n) Space O(1)
        if index < 0 or index >= self.length:
            return
        current= self.head
        for i in range(index):
            current = current.next
        return current.value
    
    def set(self,index,value): #Time O(n) Space O(1)
        if index < 0 or index >= self.length:
            return False
        current= self.head
        for i in range(index):
            current = current.next
        current.value = value
        return True
    
    def remove_first(self): #Time O(1) Space O(1)
        if self.head is None:
            return None
        removed = self.head
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return removed.value
        new_head = removed.next
        new_head.prev = None
        self.head = new_head
        self.length=-1
        return removed
    
    def remove_last(self): #Time O(1) Space O(1)
        if self.tail is None:
            return None
        removed = self.tail
        self.tail = removed.prev
        self.tail.next = None
        return removed.value
    
    def remove(self,value): #Time O(n) Space O(1)
        if self.head is None:
            return None
        current = self.head
        prev = self.head.prev
        for i in range(self.length):
            if current.value == value:
                prev.next = current.next
                return current.value
            prev = current.prev
            current = current.next
    
    def contains(self,value): #Time O(n) Space O(1)
        if self.head is None:
            return False
        current = self.head
        for i in range(self.length):
            if current.value == value:
                return True
        return False
    
    def clear(self): #Time O(1) Space O(1)
        if self.head is None:
            return None
        self.head = None
        self.tail = None
        self.length = 0
        
    def to_list(self): #Time loop through the entire list O(n) Space O(n) creat a new list
        result = []
        current = self.head
        while current is not None:
            result.append(current)
            current = current.next
        return result

    def __str__(self): #Time loop through the entire list O(n) Space O(1)
        linkedlist_str = ""
        current = self.head
        while current is not None:
            linkedlist_str+=current+" "
            current = current.next
        return linkedlist_str