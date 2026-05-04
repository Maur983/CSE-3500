# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head): #Time O(nlogn) Space O(logn)
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
    
    def getMid(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self, left,right):
        if not left:
            return right
        if not right:
            return left
        if left.val < right.val:
            head = left
            prev = left
            left = left.next
        else:
            head = right
            prev = right
            right = right.next
        while left and right:
            if left.val < right.val:
                prev.next = left
                left = left.next
            else:
                prev.next = right
                right = right.next
            prev = prev.next
        if left:
            prev.next = left
        else:
            prev.next = right
        return head