nums = [2, 5, 9, 30, 45, 62, 10 ,5]
target = 10


class Solution:
    def search(nums, target):
        n = len(nums)

        l = 0
        r = n-1

        while l<=r:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1