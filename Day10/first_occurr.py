class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1): #Time O(n+m) Space O(1)
            if haystack[i:i+len(needle)] == needle: #Time O(1) Space O(1)
                return i #Time O(1) Space O(1)
        return -1 #Time O(1) Space O(1)