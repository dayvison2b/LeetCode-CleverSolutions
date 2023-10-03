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

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #Hashtable Approach
        count = 0
        hash = {}
        for num in nums:
            hash[num] = hash.get(num,0) + 1
        for e,v in hash.items():
            if v <= 1:
                continue
            count += v * (v - 1) // 2
        return count
    
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(v * (v - 1) // 2 for v in {num:nums.count(num) for num in nums}.values())
    
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(v * (v - 1) // 2 for v in Counter(nums).values())