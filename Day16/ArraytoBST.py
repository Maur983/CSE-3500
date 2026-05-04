# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: #Time O(n) Space O(logn)
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        left = 0
        right = len(nums)-1
        return self.tree(nums,left,right)
    
    def tree(self,nums,left, right):
        if left > right:
            return None 
        mid = (left + right) // 2
        node = TreeNode(nums[mid]) 
        node.left = self.tree(nums,left, mid - 1)
        node.right = self.tree(nums,mid + 1, right)
        return node