class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = set() #Time O(1) Space O(1)
        for i in nums: #Time O(n) Space O(1)
            if i in dup: #Time O(1) Space O(1)
                return True #Time O(1) Space O(1)
            dup.add(i) #Time O(1) Space O(1)
        return False #Time O(1) Space O(1)