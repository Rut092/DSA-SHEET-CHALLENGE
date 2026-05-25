class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.out_stack = []
        self.top_ele = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.top_ele == None:
            self.top_ele = x

    def pop(self):
        """
        :rtype: int
        """
        if len(self.out_stack)==0:
            for i in range(len(self.stack)):
                self.out_stack.append(self.stack.pop())

        return self.out_stack.pop() if self.out_stack else None  

    def peek(self):
        """
        :rtype: int
        """
        if len(self.out_stack)==0:
            for i in range(len(self.stack)):
                self.out_stack.append(self.stack.pop())

        self.top_ele = self.out_stack[-1] if self.out_stack else None
        return self.top_ele
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack)==0 and len(self.out_stack)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()