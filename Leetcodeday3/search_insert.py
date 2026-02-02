class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0 #O(1)
        high = len(nums) - 1 #O(1)
        while low <= high: #log(n)
            mid = low + (high - low) // 2 #O(1)
            if nums[mid] == target: #O(1)
                return mid
            elif nums[mid] < target: #O(1)
                low = mid + 1 #O(1)
            else: #O(1)
                high = mid - 1 #O(1)
        return low #O(1)
