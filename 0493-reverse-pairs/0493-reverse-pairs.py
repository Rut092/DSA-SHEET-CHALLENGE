class Solution:
    def reversePairs(self, arr: List[int]) -> int:
        self.count = 0
        
        def divide(arr,low,high):
            if low<high:
                mid = (low+high)//2
                divide(arr,low,mid)
                divide(arr,mid+1,high)
                merge(arr,low,mid,high)

        def merge(arr,low,mid,high):

            j=mid+1
            for i in range(low,mid+1):
                while(j<=high and arr[i]>2*arr[j]):
                    j+=1
                self.count+=j-(mid+1)

            temp=[]
            i,j=low,mid+1
            while(i<=mid and j<=high):
                if arr[i]<arr[j]:
                    temp.append(arr[i])
                    i+=1
                else:
                    temp.append(arr[j])
                    j+=1

            if i<=mid:
                temp.extend(arr[i:mid+1])
            if j<=high:
                temp.extend(arr[j:high+1])

            arr[low:high+1]=temp

        divide(arr,0,len(arr)-1)
        return self.count