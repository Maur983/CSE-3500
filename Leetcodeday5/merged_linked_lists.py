# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None: #Time O(1) Space O(1)
            return list2 #Time O(1) Space O(1)
        if list2 is None: #Time O(1) Space O(1)
            return list1 #Time O(1) Space O(1)
        
        if list1.val < list2.val: #Time O(1) Space O(1)
            head = list1 #Time O(1) Space O(1)
            list1=list1.next #Time O(1) Space O(1)
        else: #Time O(1) Space O(1)
            head = list2 #Time O(1) Space O(1)
            list2 = list2.next #Time O(1) Space O(1)
        current = head #Time O(1) Space O(1)
        while list1 and list2: #Time O(n+m) Space O(1)
            if list1.val <= list2.val: #Time O(1) Space O(1)
                current.next = list1 #Time O(1) Space O(1)
                list1 = list1.next #Time O(1) Space O(1)
            else: #Time O(1) Space O(1)
                current.next = list2 #Time O(1) Space O(1)
                list2 = list2.next #Time O(1) Space O(1)
            current = current.next #Time O(1) Space O(1)
        if list1 is not None: #Time O(1) Space O(1)
            current.next = list1 #Time O(1) Space O(1)
        else: #Time O(1) Space O(1)
            current.next = list2 #Time O(1) Space O(1)
        return head  #Time O(1) Space O(1)