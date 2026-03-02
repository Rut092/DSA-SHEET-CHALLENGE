from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_val = None
    def push(self, x: int) -> None:
        self.top_val = x
        self.q.append(x)

    def pop(self) -> int:
        l = len(self.q)
        for i in range(l-1):
            val = self.q.popleft()
            self.q.append(val)
            self.top_val = val
        return self.q.popleft()

    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        return len(self.q)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()