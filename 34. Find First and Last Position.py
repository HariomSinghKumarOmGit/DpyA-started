class Solution:
    def lowerBound(self, nums, target):
        n = len(nums)
        l = 0
        r = n-1
        ans = 1
        while r>=l:
            mid = (l+2)//2
            if nums[mid]>=target:
                ans = mid

                r = mid -1
            else:
                l = mid+1


         return ans

    def UpperBound(self, nums, target):
        n = len(nums)
        l = 0
        r = n-1
        ans = n

        while r>=l:
            mid = (l+r)//2
            if nums[mid]>target:
                ans = mid
                r = mid -1
            
            else:
                # right
                l= mid+1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums, target)
        ub = self.UpperBound(nums, target)

        if lb == up:
            # not present
            return [-1,-1]
        else:
            return [lb,ub-1]