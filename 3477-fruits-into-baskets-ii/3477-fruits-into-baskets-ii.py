class Segment:
    def __init__(self,data):
        self.n = len(data)
        self.tree = [0]*(4*self.n)

        if self.n>0:
            self._build(data,1,0,self.n-1)
    
    def _build(self,data,node,start,end):

        if start == end:
            self.tree[node] = data[start]
            return

        mid = (start+end)//2
        self._build(data,2*node,start,mid)
        self._build(data,2*node+1,mid+1,end)

        self.tree[node] = max(self.tree[2*node],self.tree[2*node+1])

    def update(self,node,start,end,val):
        if val>self.tree[node]:
            return False

        if start == end:
            self.tree[node]= -1
            return True

        mid = (start+end)//2

        found = self.update(node*2,start,mid,val)

        if not found: 
            found = self.update(node*2+1,mid+1,end,val)

        self.tree[node] = max(self.tree[2*node],self.tree[2*node+1])

        return found


class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        fruits_length = len(fruits)
        basket_length = len(baskets)
        st = Segment(baskets)
        leftout = 0

        for i in range(fruits_length):
            if  not st.update(1,0,basket_length-1,fruits[i]):
                leftout+=1    
        
        return leftout