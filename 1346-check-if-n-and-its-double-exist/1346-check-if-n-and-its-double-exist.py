class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        book = set()
        for num in arr:
            if num*2 in book or (num%2==0 and float(num/2) in book):
                return True
            else:
                book.add(float(num))
        return False