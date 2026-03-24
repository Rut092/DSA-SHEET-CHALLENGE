class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n  = len(nums)
        self.tree = [0]*(4*self.n+1)

        if self.n>0:
            self._build(nums,1,0,self.n-1)

    def _build(self,nums,node,start,end):

        if start == end :
            self.tree[node] = nums[start]
            return 

        mid = (start+end)//2
        self._build(nums,node*2,start,mid)
        self._build(nums,node*2+1,mid+1,end)

        self.tree[node] = self.tree[2*node] + self.tree[2*node+1] 
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self._update(1,0,self.n-1,index,val)

    def _update(self,node,start,end,idx,val):
        
        if start == end:
            self.tree[node]= val
            return 
        
        mid = (start+end)//2
        if idx<=mid:
            self._update(2*node,start,mid,idx,val)
        else:
            self._update(2*node+1,mid+1,end,idx,val)

        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._query(1,0,self.n-1,left,right)
        
    def _query(self,node,start,end,left,right):

        if start>right or end<left:
            return 0

        if left<=start and end<=right:
            return self.tree[node]
        
        mid = (start+end)//2

        left_sum = self._query(node*2,start,mid,left,right)
        right_sum = self._query(node*2+1,mid+1,end,left,right)

        return left_sum + right_sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)