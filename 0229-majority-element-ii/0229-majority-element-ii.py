class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1 = num2 = None
        count1 = count2 = 0
        for num in nums:
            if num==num1:
                count1+=1
            elif num==num2:
                count2+=1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                num2 = num
                count2=1
            else:
                count1-=1
                count2-=1

        n_o_3 = len(nums)//3
        res = []
        for num in [num1,num2]:
            if num is not None and nums.count(num)>n_o_3:
                res.append(num)
        
        return res