class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def countOdd(k):
            count = odd = i = 0
            for j in range(len(nums)):
                if nums[j]%2==1:
                    odd+=1

                while(odd>k):
                    if nums[i]%2==1:
                        odd-=1
                    i+=1
                    
                if odd<=k:
                    count+=(j-i+1)

            return count
        
        return countOdd(k)-countOdd(k-1)