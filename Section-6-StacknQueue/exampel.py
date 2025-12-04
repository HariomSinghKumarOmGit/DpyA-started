class Stack:
    def __init__(self):
        self.val = []

    def push(self,x):
        self.val.append(x)

    def pop(self):
        self.val.pop()
        
    def top(self):
        if len(self.val)==0:
            return -1
        return self.val[-1]
    def size(self):
        return len(self.val)
    

st = Stack()

st.push(5)
st.push(3)
st.push(11)
st.push(12)
st.push(7)

print(st.top())
st.pop()
print(st.top())
print(st.size())
