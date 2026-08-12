class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = [ ]

        def calc(count,total,array,num):
            if num==total and count==k-1:
                res.append(array[:]+[num])
                return
            elif num>total or count>=k:
                return
            else:
                for i in range(num+1,10):
                    calc(count+1,total-num,array+[num],i)

        for number in range(1,8):
            calc(0,n,[],number)

        return res