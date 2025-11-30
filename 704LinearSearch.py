nums = [2, 5, 9, 30, 45, 62, 10 ,5]
target = 10

class Solution:
    def search(nums, target):
        for i in range(len(nums)):
            if i == target:
                return i

        return -1

