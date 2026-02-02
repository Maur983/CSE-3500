class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index,num in enumerate(nums): #O(n)
            needed = target - num #O(1)
            if needed in nums and index != nums.index(needed): #O(1)
                ind = nums.index(needed) #O(1)
                return index,ind #O(1)