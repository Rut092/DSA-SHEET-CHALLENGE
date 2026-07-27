class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        left = 0
        for fruit in fruits:
            found = False
            for idx in range(len(baskets)):
                if baskets[idx]>=fruit:
                    baskets[idx]=-1
                    found = True
                    break
            if not found:
                left+=1

        return left
            
