class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} #Time O(1) Space #O(1)
        num = 0 #Time O(1) Space #O(1)
        for i in range(len(s)-1): #Time O(n) Space #O(1)
            if roman[s[i+1]]>roman[s[i]]: #Time O(1) Space #O(1)
                num-=roman[s[i]] #Time O(1) Space #O(1)
            else: #Time O(1) Space #O(1)
                num+=roman[s[i]] #Time O(1) Space #O(1)

        num+=roman[s[-1]] #Time O(1) Space #O(1)
        return num #Time O(1) Space #O(1)