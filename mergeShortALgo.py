nums = [1,2,4,6,9,5,3,8,7]

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        from typing import List

class Solution:
    def merge(self, l, r, nums, mid):
       
        a=[]
        b=[]
        
        for i in range(l,mid+1):
            a.append(nums[i])
        for i in range(mid+1 , r+1):
            b.append(nums[i])
        
        i,j,k = 0,0,l

        while k<=r:
            if j == len(b):
                nums[k] = a[i]
                i += 1
                k += 1
            elif i == len(a):
                nums[k] = b[j]   
                j += 1
                k += 1
            elif a[i] < b[j]:
                nums[k] = a[i]
                i += 1
                k += 1
            else:                  
                nums[k] = b[j]
                j += 1
                k += 1


    def mergeShort(self, nums, l, r):   
        if l >= r:
            return 
        
        mid = (l + r) // 2
        self.mergeShort(nums, l, mid)    
        self.mergeShort(nums, mid + 1, r)

        self.merge(l, r, nums, mid)     

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeShort(nums, 0, len(nums) - 1)
        return numsg