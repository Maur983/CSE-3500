# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        slow = head #Time O(1) Space O(1)
        fast = head #Time O(1) Space O(1)
        for i in range(n): #Time O(m) space O(1)
            fast = fast.next #Time O(1) Space O(1)
        if fast is None: #Time O(1) Space O(1)
            return head.next #Time O(1) Space O(1)
        
        while fast.next is not None: #Time O(n) Space O(1)
            slow = slow.next #Time O(1) Space O(1)
            fast = fast.next #Time O(1) Space O(1)
        slow.next = slow.next.next #Time O(1) Space O(1)
        return head #Time O(1) Space O(1)