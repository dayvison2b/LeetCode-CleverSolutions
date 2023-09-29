#  https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(1, n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i-1]
                continue
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                count = count + 1
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                count = count + 1
        return count