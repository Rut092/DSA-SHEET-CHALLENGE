class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_list = {}
        for i in nums:
            my_list[i] = 1 + my_list.get(i,0)
            if my_list[i]>1:
                return True

        return False