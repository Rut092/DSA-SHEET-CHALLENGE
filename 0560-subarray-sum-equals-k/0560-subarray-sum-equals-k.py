class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        book = {0:1}
        total = curr_sum = 0
        for num in nums:
            curr_sum+=num
            if curr_sum-k in book:
                total+=book[curr_sum-k]
            if curr_sum in book:
                book[curr_sum]+=1
            else:
                book[curr_sum]=1
        
        return total
        


                