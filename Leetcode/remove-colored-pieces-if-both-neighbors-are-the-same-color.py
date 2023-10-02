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

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count,b_count = 0,0
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == "A":
                    a_count += 1
                else:
                    b_count += 1
        return a_count > b_count
    
import re
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        for match in re.findall("A+", colors):
            if len(match) > 2:
                alice += len(match) - 2
        for match in re.findall("B+", colors):
            if len(match) > 2:
                bob += len(match) - 2
        return alice > bob