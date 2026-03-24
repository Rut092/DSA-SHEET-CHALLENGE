class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        fruits_length = len(fruits)
        basket_length = len(baskets)

        leftout = 0

        for i in range(fruits_length):
            for j in range(0,basket_length):
                if baskets[j]>=fruits[i]:
                    baskets[j] = 0 
                    leftout-=1
                    break
            leftout+=1      
        
        return leftout