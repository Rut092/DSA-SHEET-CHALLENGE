class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mini = None

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack:
            self.mini = value
        else:
            self.mini = min(self.mini,value)
        self.stack.append([value,self.mini])

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.mini = None if not self.stack else self.stack[-1][1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()