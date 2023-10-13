# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo1 = cost[0]
        memo2 = cost[1]
        for i in range(2,n):
            current = cost[i] + min(memo1,memo2)
            memo1 = memo2
            memo2 = current
        return min(memo1,memo2)
