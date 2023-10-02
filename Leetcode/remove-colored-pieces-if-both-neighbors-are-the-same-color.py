# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count,b_count = 0,0
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i+1] == colors[i] == "A":        
                a_count += 1
            elif colors[i-1] == colors[i+1] == colors[i] == "B":
                b_count += 1
        return a_count > b_count
    