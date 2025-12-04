class Stack:
    def __init__(self):
        self.val = []

    def push(self,x):
        self.val.append(x)

    def pop(self):
        if len(self.val)==0:
            return -1
        x= self.val[-1]
        self.val.pop()
        return x
        
    def top(self):
        if len(self.val)==0:
            return -1
        return self.val[-1]
    def size(self):
        return len(self.val)
    

class Solution:
    def isValid(self, s: str) -> bool:
        st = Stack()
        for i in s:
            if i =="[" or i =="(" or i =="{":
                st.push(i)
            else:
                if st.size()==0:
                    return False
                tp = st.pop()
                if i =="]" and tp!="[" or i =="}" and tp!="{" or i ==")" and tp!="(":
                    return False
        

        return st.size()==0