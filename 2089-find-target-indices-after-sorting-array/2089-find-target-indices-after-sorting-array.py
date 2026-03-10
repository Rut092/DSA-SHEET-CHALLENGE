class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = equal = 0
        ans = []
        for num in nums:
            if num==target:
                equal+=1
            elif num<target:
                smaller+=1
        for i in range(smaller,smaller+equal):
            ans.append(i)

        return ans
        