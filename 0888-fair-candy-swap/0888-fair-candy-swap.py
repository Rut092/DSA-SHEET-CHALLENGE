class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        ta = sum(aliceSizes)
        tb = sum(bobSizes)
        sb = set(bobSizes) 

        diff = (tb-ta)/2
        for num in aliceSizes:
            if num+diff in sb:
                return [num,num+diff]