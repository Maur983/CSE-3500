# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head #Time O(1) Space O(1)
        prev = None #Time O(1) Space O(1)
        while curr is not None: #Time O(n) Space O(1)
            next_node= curr.next #Time O(1) Space O(1)
            curr.next = prev #Time O(1) Space O(1)
            prev = curr #Time O(1) Space O(1)
            curr = next_node #Time O(1) Space O(1)
        return prev #Time O(1) Space O(1)