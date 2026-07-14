class Solution(object):
    def reversePairs(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.count = 0

        def divide(start,end):
            if start<end:
                mid = (start+end)>>1
                divide(start,mid)
                divide(mid+1,end)
                
                merge(start,mid,end)
        
        def merge(low,mid,high):
            left_len = low
            right_len = mid+1
            count = 0
            temp = []
            
            ind = mid+1
            for i in range(low,mid+1):
                while(ind<=high and arr[i]>2*arr[ind]):
                    ind+=1
                count+=(ind-mid-1)
            
            while(left_len<=mid and right_len<=high):
                if arr[left_len]>arr[right_len]:
                    temp.append(arr[right_len])
                    right_len+=1
                else:
                    temp.append(arr[left_len])
                    left_len+=1
                    
            if left_len<=mid:
                temp+=arr[left_len:mid+1]
            if right_len<=high:
                temp+=arr[right_len:high+1]
            
            for i in range(low,high+1):
                arr[i]=temp[i-low]
            
            self.count+=count
            
        divide(0,len(arr)-1)
        return self.count