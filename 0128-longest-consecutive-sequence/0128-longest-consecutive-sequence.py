class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        bucket = {i:1 for i in nums}
        max_count = 0
        for i in bucket:
            count=1
            if i-1 not in bucket:
                num = i+1
                while(num in bucket):
                    count+=1
                    num+=1
            max_count = max(max_count,count)

        return max_count
        