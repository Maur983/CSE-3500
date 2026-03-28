class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = "" #Time O(1) Space O(1)
        for i in range(len(strs[0])): #Time O(m) Space O(1)
            char = strs[0][i] #Time O(1) Space O(1)
            for j in range(1, len(strs)): #Time O(n) Space O(1)
                if i >= len(strs[j]) or strs[j][i] != char: #Time O(1) Space O(1)
                    return prefix #Time O(1) Space O(1)
            prefix += char #Time O(1) Space O(m)
        return prefix #Time O(1) Space O(1)