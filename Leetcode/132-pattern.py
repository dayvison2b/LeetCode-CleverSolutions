# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []
        curMin = nums[0]

        for num in nums[1:]:
            while stack:
                if num >= stack[-1][0]:
                    stack.pop()
                else:
                    break

            if stack and num > stack[-1][1]:
                return True

            stack.append([num, curMin])
            curMin = min(curMin, num)

        return False
