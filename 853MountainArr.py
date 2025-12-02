class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-2
        ans = n-1

        while r>=l:
            mid = (l+r)//2
            if nums[mid]<nums[mid+1]:
                # Right
                l = mid +1
            else:
                ans = mid
                # Left
                r = mid -1

        return ans


       