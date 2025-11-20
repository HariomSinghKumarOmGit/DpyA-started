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

