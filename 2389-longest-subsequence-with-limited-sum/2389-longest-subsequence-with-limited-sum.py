class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        res = []
        for i in range(1,l):
            nums[i]+=nums[i-1]

        for q in queries:
            low,high = 0,l-1
            ans = -1
            while(low<=high):
                mid = (low+high)//2
                if nums[mid]<=q:
                    low = mid+1
                    ans = mid
                else:
                    high = mid-1

            res.append(ans+1)

        return res
            