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

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])
    
    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i]+=min(cost[i-1],cost[i-2])
        print(cost)
        return min(cost[-1],cost[-2])