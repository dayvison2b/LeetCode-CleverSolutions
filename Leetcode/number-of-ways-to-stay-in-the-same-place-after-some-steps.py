# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # Define a modulus value for taking the modulo operation to avoid overflow.
        mod = 1000000007
        
        # Calculate the maximum position the pointer can reach, which is the minimum of steps/2 and arrLen - 1.
        maxPosition = min(steps // 2, arrLen - 1)
        
        # Create a 2D array dp to store the number of ways to reach a specific position at each step.
        dp = [[0] * (maxPosition + 1) for _ in range(steps + 1)]
        
        # Initialize the number of ways to stay at position 0 after 0 steps to 1.
        dp[0][0] = 1
        
        # Loop through the number of steps.
        for i in range(1, steps + 1):
            for j in range(maxPosition + 1):
                # Initialize the number of ways to stay at the current position with the number of ways to stay at the same position in the previous step.
                dp[i][j] = dp[i - 1][j]
                
                # If the current position is greater than 0, add the number of ways to reach it by moving left.
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                
                # If the current position is less than the maximum position, add the number of ways to reach it by moving right.
                if j < maxPosition:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
        
        # The final result is stored in dp[steps][0], representing the number of ways to reach the initial position after taking 'steps' steps.
        return dp[steps][0]
        
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n=len(cost)
        return self.dp(n-1,cost,time,0,{})
    
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        maxColumn = min(arrLen, steps // 2 + 1)  # Boundary to ensure we can come back
        
        curr = [0] * (maxColumn + 1)
        prev = [0] * (maxColumn + 1)
        prev[0] = 1
        
        for i in range(1, steps + 1):
            for j in range(maxColumn + 1):
                curr[j] = prev[j]
                if j - 1 >= 0:
                    curr[j] = (curr[j] + prev[j-1]) % mod
                if j + 1 < maxColumn:
                    curr[j] = (curr[j] + prev[j+1]) % mod
            curr, prev = prev, curr  # Swap arrays for the next iteration
        
        return prev[0]