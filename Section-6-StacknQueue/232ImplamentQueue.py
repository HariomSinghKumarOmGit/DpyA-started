class Stack:
    def __init__(self):
        self.val = []

    def push(self,x):
        self.val.append(x)

    def pop(self):
        if len(self.val) == 0:
            return -1
        return self.val.pop()
        
    def top(self):
        if len(self.val)==0:
            return -1
        return self.val[-1]
    def size(self):
        return len(self.val)
    

class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        while self.s1.size()>0:
            self.s2.push(self.s1.pop())
        self.s1.push(x)
        while self.s2.size()>0:
            self.s1.push(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1.top()

    def empty(self) -> bool:
        return self.s1.size()==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()