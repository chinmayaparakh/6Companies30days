class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if grid[i][j] != 0:
                    break
            else:
                continue
            for k in range(i+1, n):
                if grid[k][i+1:] == [0] * (n-i-1):
                    ans += (k-i)
                    grid[i:k+1] = grid[k:k+1] + grid[i:k]  
                    break
            else:
                return -1
        return ans
