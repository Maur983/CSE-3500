class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 1 #O(1)
        for i in range(1, len(nums)): #O(n)
            if nums[i] != nums[i - 1]: #O(1)
                nums[unique] = nums[i] #O(1)
                unique += 1 #O(1)
        return unique #O(1)