class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nonel = 0 #O(1)
        for i in range(len(nums)): #O(n)
            if nums[i] != val: #O(1)
                nums[nonel] = nums[i] #O(1)
                nonel += 1 #O(1)
        return nonel #O(1)