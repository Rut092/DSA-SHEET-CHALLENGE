class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num>k:
                break
            k+=1
        return k