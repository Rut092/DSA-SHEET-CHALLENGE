class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_check = set(nums)
        max_streak=0
        for num in set_check:
            if num-1 not in set_check:
                current_streak = 1
                while(num+1 in set_check):
                    current_streak+=1
                    num+=1
                max_streak = max(max_streak,current_streak)

        return max_streak