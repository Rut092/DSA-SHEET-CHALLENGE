class Solution(object):
    def isPalindrome(self, nums):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(nums)-1

        while(i<j):
            if not nums[i].isalnum():
                i+=1
            elif not nums[j].isalnum():
                j-=1
            else:
                if nums[i].lower()==nums[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
        return True