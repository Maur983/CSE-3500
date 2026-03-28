class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = dict() #Time O(1) Space O(1)
        max = 0 #Time O(1) Space O(1)
        curr = 0 #Time O(1) Space O(1)
        for i in nums: #Time O(n) Space O(1)
            major[i]= major.get(i, 0) + 1 #Time O(1) Space O(m)
            if major[i] > max: #Time O(1) Space O(1)
                max = major[i] #Time O(1) Space O(1)
                curr = i #Time O(1) Space O(1)
        return curr #Time O(1) Space O(1)