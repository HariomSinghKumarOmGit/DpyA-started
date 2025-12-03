class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Stotal = sum(nums)
        Sleft = 0
        n = len(nums)

        for i in range(n):
            Sright = Stotal - Sleft - nums[i]
            if Sleft == Sright:
                return i
            Sleft+=nums[i]
        return -1

# this is the problem in which we have to find sum form both end and in middle value sum both side same