import heapq
class Solution:
    def findRelativeRanks(self, score): #Time O(nlogn) Space O(n)
        pq = []
        result = [0]*len(score)
        for i in range(len(score)):
            heapq.heappush(pq,(-score[i], i))
        rank =1
        while pq:
            _,i = heapq.heappop(pq)
            if rank ==1:
                result[i] = "Gold Medal"
            elif rank ==2:
                result[i] = "Silver Medal"
            elif rank==3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank)
            rank+=1
        return result