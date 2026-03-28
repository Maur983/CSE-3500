class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        vis = set()
        st = []
        last_occ = {}
        
        for i in range(len(s)): #Time O(1) Space O(n)
            last_occ[s[i]] = i
            
        for i in range(len(s)): #Time O(n) Space O(1)
            if s[i] not in vis:
                while (st and st[-1] > s[i] and last_occ[st[-1]] > i):
                    vis.remove(st.pop())
                st.append(s[i])
                vis.add(s[i])
                
        return "".join(st)