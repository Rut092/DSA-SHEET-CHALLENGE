import collections
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket = collections.defaultdict(int)
        i = 0
        for j in range(len(fruits)):
            basket[fruits[j]]+=1

            if len(basket)>2:
                basket[fruits[i]]-=1
                if basket[fruits[i]]==0:
                    del basket[fruits[i]]
                i+=1
        
        return j-i+1