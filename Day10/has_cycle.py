# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: #Time O(1) Space O(1)
            return False #Time O(1) Space O(1)

        slow = head #Time O(1) Space O(1)
        fast = head #Time O(1) Space O(1)

        while fast and fast.next: #Time O(n) Space O(1)
            slow = slow.next #Time O(1) Space O(1)
            fast = fast.next.next #Time O(1) Space O(1)
            if slow == fast: #Time O(1) Space O(1)
                return True #Time O(1) Space O(1)
        return False #Time O(1) Space O(1)