nums = [7,3,9,5,2,4,8]

class Solution:
    def partition(self,nums,l,r):
        key = nums(r)
        start = l

        for i in range(l,r-1):
            if nums[i]<=key:
                temp = nums[i]
                nums[i]=nums[start]
                numsp[start]=temp
                start+=1

        return start-=1


    def quickShort(self,nums,l,r):
        # base code
        if l>=r:
            return
        
        # recuresive
        p = self.partition(nums,l,r)
        self.quickShort(nums,l,p+1)
        self.quickShort(nums,p+1,r+1)
        
    def sortArray(self, nums):
        n = len(nums)
        self.quickShort(nums,0,n-1)

        return nums

    

      