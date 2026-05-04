class Solution:
    def climbStairs(self, n: int) -> int: #Time O(n) do to the fact we have a for loop through the range of 3 to the number asked Space O(n) due to the fact that we create a new list which range of 3 to the number of elements
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        Cl = [0]*(n+1)
        Cl[1] =1
        Cl[2] =2
        for i in range(3,n+1):
            Cl[i] = Cl[i-1]+Cl[i-2]
        return Cl[n]