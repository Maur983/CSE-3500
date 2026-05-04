class Solution:
    def expand(self, s,left,right):
        while left>=0 and right<=len(s)-1 and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
    
    def longestPalindrome(self, s: str) -> str: #Time O(n^2) Space O(1)
        if not s:
            return ""
        start=0
        end=0
        for i in range(len(s)):
            odd = self.expand(s,i,i)
            even = self.expand(s,i,i+1)
            max_len = max(even,odd)
            if max_len> end-start:
                start =i -(max_len-1)//2
                end = i+ max_len//2
        return s[start:end+1]