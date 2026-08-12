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
                array.append(num)
                res.append(array[:])
                array.pop()
                return
            elif num>total or count>=k:
                return
            else:
                array.append(num)
                for i in range(num+1,10):
                    calc(count+1,total-num,array,i)
                array.pop()

        for number in range(1,8):
            calc(0,n,[],number)

        return res