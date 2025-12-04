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
    
class Solution:
    def nextGreater(self, arr):
        n = len(arr)
        ans = [-1]*n

        st= Stack()
        st.push(arr[-1])
        for i in range(n-2, -1, -1):
            while st.size()==0 and st.top()<= arr[i]:
                st.pop()
                
            if st.size()==0:
                arr[i]=-1
            else:
                ans[i] = st.top()
            st.push(arr[i])

        return ans

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = self.nextGreater(nums2)
        dict1 = {}
        for i in range(len(nums2)):
            dict1[num2[i]] = ans[i]
        
        return list(map(lambda x: dict1[x], nums1))
        