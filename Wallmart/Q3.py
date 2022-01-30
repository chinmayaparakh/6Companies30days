class Solution:
    def winnerOfGame(self, colors: str) -> bool:
         return sum(len(a)-2 for a in colors.split('B') if len(a)>2) > sum(len(b)-2 for b in colors.split('A') if len(b)>2)
