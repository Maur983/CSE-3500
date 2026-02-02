class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0] #O(1)
        for s in strs[1:]: #O(n)
            while not s.startswith(prefix): #o(n)
                prefix = prefix[:-1] #O(1)
                if not prefix: #O(1)
                    return "" #O(1)
        return prefix #O(1)