class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = 0
    def next(self, price: int) -> int:
        self.count+=1
    
        if not self.stack or self.stack[-1][0]>price: 
            self.stack.append([price,self.count])
            return 1

        while(self.stack and self.stack[-1][0]<=price):
            self.stack.pop()
    
        ele_idx = 0 if not self.stack else self.stack[-1][1]
        self.stack.append([price,self.count])

        return self.count - ele_idx 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)