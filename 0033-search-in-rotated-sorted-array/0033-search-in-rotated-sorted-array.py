class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low,high=0,len(nums)-1

        while(low<=high):

            mid = (low+high)//2

            if nums[low]<=nums[mid] and nums[low]<=target<=nums[mid]:
                print('a',low,mid,high)
                low,high=low,mid
                while(low<=high):
                    mid=(low+high)//2
                    if nums[mid]==target:
                        return mid
                    elif nums[mid]>target:
                        high=mid-1
                    else:
                        low=mid+1
                return -1

            elif nums[mid]<=nums[high] and nums[high]>=target>=nums[mid] :
                print('b',low,mid,high)
                low,high=mid,high
                while(low<=high):
                    mid=(low+high)//2
                    if nums[mid]==target:
                        return mid
                    elif nums[mid]>target:
                        high=mid-1
                    else:
                        low=mid+1
                return -1

            elif nums[low]<=nums[mid]:
                print('c',low,mid,high)
                low=mid+1
            else:
                print('d',low,mid,high)
                high=mid-1

        return -1