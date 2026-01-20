class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums)==len(set(nums))

        # counts = {}
        # for i in nums:
        #     counts[i] = 1 + counts.get(i,0)
        #     if counts[i]>1:
        #         return True

        # return False