class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low,high = 0,len(numbers)-1
        while(low<=high):
            total = numbers[low]+numbers[high]
            if target==total:
                return [low+1,high+1]
            elif total<target:
                low+=1
            else:
                high-=1

        
