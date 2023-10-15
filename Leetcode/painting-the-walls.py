# https://leetcode.com/problems/painting-the-walls/

class Solution:
    def dp(self,i,cost,time,avl,dct):
        if i<0:
            if avl<0:
                return float("infinity")
            return 0
        if (i,avl) in dct:
            return dct[(i,avl)]
        x=self.dp(i-1,cost,time,avl+time[i],dct)+cost[i]
        y=self.dp(i-1,cost,time,avl-1,dct)
        dct[(i,avl)]=min(x,y)
        return min(x,y)
        
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n=len(cost)
        return self.dp(n-1,cost,time,0,{})

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n=len(cost)
        @cache
        def f(i, walls):
            if walls>=n: return 0
            if i>=n: 
                return 2**31+1
            ans=cost[i]+f(i+1, walls+1+time[i])
            ans=min(ans, f(i+1, walls))          
            return ans
        return f(0, 0)
        