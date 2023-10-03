# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #Brute force approach
        goodPairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    goodPairs += 1
        return goodPairs