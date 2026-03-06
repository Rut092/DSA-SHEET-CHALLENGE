class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = len(letters)
        low,high = 0,l-1
        res = 0

        while(low<=high):
            mid = (low+high)//2
        
            if letters[mid]<=target:
                low = mid+1
            else:
                res = mid
                high=mid-1
                
        return letters[res] if res<l else letters[0]