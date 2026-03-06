class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        ta = tb = 0
        sb = set([])
        for num in aliceSizes:
            ta+=num
        for num in bobSizes:
            tb+=num
            sb.add(num)

        diff = (tb-ta)/2
        for num in aliceSizes:
            if num+diff in sb:
                return [num,num+diff]