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
    

class Solution:
    def majorityElement(self, nums):
        return [num for num, count in Counter(nums).items() if count > len(nums) // 3]
    
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [num for num in (candidate1, candidate2) if nums.count(num) > len(nums) // 3]