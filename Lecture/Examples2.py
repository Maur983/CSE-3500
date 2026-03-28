class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
head = node0
node0.next = node1
node1.next = node2
current = head
while current is not None:
    print(current.value)
    current = current.next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length =0
    
    def size(self):
        return self.length
    
    def prepend (self ,value) :
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
    
    def append(self,value) :
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail . next = new_node
            self.tail = new_node
        self.length += 1
    def insert_at(self,index,value) :
        if index < 0 or index >= self.length :
            return
        if index == 0:
            self.prepend(value)
            return
        if index == self.length :
            self.append(value)
            return
        else:
            new_node = Node(value)
            current = self.head
            for i in range(index-1):
                current = current.next
            next_node = current.next
            new_node.next = next_node
            current.next = new_node
            self.length+=1
    
    def remove_at(self,index):
        if index<0 or index>self.length:
            return
        if index ==0:
            self.head = self.head.next
            self.length-=1
            if self.length==0:
                self.tail=None
        else:
            current = self.head
            for i in range(index-1):
                current.next
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            self.length-=1

    def reverse_linked_lists(self): #Time O(n) Space O(1)
        if self.head is None:
            return None
        current = self.head
        prev =None
        for i in range(self.length):
            temp = current.next
            current.next = prev
            temp.next = current
            prev = current
            current = temp
        return self.head
    
    def remove_duplicates(self): #Time O(n) Space O(1)
        if self.head is None:
            return None
        current= self.head
        while current is not None:
            next_node = current.next
            if current.value == next_node.value:
                if next_node.value == self.tail.value:
                    self.tail = current
                    return self.head
                else:
                    next_node = next_node.next
                    self.length-=1
            current = next_node
    
    def mergelinkedlists(self, head1,head2): #Time O(n+m) Space O(1) This is because we aren't creating new nodes we just taking nodes that exist and pointing some where else.
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if (head1 is None) and (head2 is None):
            return None
        if head1.value<head2.value:
            head= head1
            head1= head1.next
        else:
            head= head2
            head2= head2.next
        current = head
        while head1 and head2:
            if head1.value < head2.value:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        if head1:
            current.next = head1
        else:
            current.next = head2
        return head
