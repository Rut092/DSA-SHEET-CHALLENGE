class Solution:
    def maxDepth(self, s: str) -> int:
        arr = []
        for i in s:
            if i=='(' or i==')':
                arr.append(i)

        max_count = 0 
        count = 0

        for i in arr:
            if i=='(':
                count+=1
                max_count = max(max_count,count)
            else:
                count-=1
        return max_count