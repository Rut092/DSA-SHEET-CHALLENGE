class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = right_sum = max_val = 0
        ind = len(cardPoints)-1

        for i in range(k):
            right_sum+=cardPoints[i]
            max_val = max(right_sum,max_val)
        
        for i in range(k-1,-1,-1):
            right_sum-= cardPoints[i]
            left_sum+=cardPoints[ind]
            max_val = max(max_val,left_sum+right_sum)
            ind-=1
        
        return max_val
        