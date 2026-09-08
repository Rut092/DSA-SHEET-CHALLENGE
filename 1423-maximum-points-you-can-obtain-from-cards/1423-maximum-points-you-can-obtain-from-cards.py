class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints)
        max_val = 0
        right_sum = 0
        for i in range(k):
            right_sum+=cardPoints[i]
            max_val = max(right_sum,max_val)
        
        left_sum = 0
        ind = l-1
        for i in range(k-1,-1,-1):
            right_sum-= cardPoints[i]
            left_sum+=cardPoints[ind]
            ind-=1

            max_val = max(max_val,left_sum+right_sum)
        
        return max_val
        