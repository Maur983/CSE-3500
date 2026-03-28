# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None: #Time O(1) Space O(1)
            return None #Time O(1) Space O(1)
        a = headA #Time O(1) Space O(1)
        b = headB #Time O(1) Space O(1)
        while a!=b: #Time O(n+m) Space O(1)
            if a is not None: #Time O(1) Space O(1)
                a = a.next #Time O(1) Space O(1)
            else: #Time O(1) Space O(1)
                a = headB #Time O(1) Space O(1)
            if b is not None: #Time O(1) Space O(1)
                b = b.next #Time O(1) Space O(1)
            else: #Time O(1) Space O(1)
                b = headA  #Time O(1) Space O(1)
        return a #Time O(1) Space O(1)