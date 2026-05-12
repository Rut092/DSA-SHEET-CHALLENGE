class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.calcGCD(max(nums),min(nums))
        
    def calcGCD(self,num1,num2):
        if num1%num2==0:
            return num2
        return self.calcGCD(num2,num1%num2)

    