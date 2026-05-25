from collections import deque
class MyStack(object):

    def __init__(self):
        self.q = deque()
        self.top_ele = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.top_ele = x
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for _ in range(len(self.q)-1):
            val = self.q.popleft()
            self.q.append(val)
            self.top_ele = val

        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.top_ele
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()