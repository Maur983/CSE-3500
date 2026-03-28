# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val): #The Time complexity
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head is not None and head.val == val: #Time O(n) Space O(1)
            head = head.next #Time O(1) Space O(1)

        curr = head
        while curr and curr.next: #Time O(n) Space O(1)
            if curr.next.val == val: #Time O(1) Space O(1)
                curr.next = curr.next.next #Time O(1) Space O(1)
            else: #Time O(1) Space O(1)
                curr = curr.next #Time O() Space O(1)
        return head #Time O(1) Space O(1)