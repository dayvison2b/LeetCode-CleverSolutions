# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict = {}
        result = []

        for num in nums:
            dict[num] = dict.get(num,0) + 1

        for k,v in dict.items():
            if v > len(nums) / 3:
                result.append(k)
                
        return result