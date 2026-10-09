class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left_sum = right_sum = max_val = 0
        l = len(cardPoints)

        for i in range(k):
            right_sum+=cardPoints[i]
            max_val = max(max_val,right_sum)

        ind = l-1
        for i in range(k-1,-1,-1):
            right_sum-=cardPoints[i]
            left_sum+=cardPoints[ind]
            ind-=1
            max_val = max(max_val,left_sum+right_sum)

        
        return max_val