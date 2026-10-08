class Solution:
    def candy(self, ratings: list[int]) -> int:
        l = len(ratings)
        res = [1]
        for i in range(1,l):
            if ratings[i]>ratings[i-1]:
                res.append(res[-1]+1)
            else:
                res.append(1)

        prev = 1
        total = res[-1]
        for i in range(l-2,-1,-1):
            right = 1+prev if ratings[i]>ratings[i+1] else 1
            prev = right
            total+=max(res[i],right)

        return total