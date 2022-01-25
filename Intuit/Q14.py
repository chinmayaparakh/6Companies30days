class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    q.append([(i, j), 0])
        if not q: return -1
        res = 0
        while q:
            (i, j), c = q.popleft()
            res = max(res, c)
            for k, l in [(-1, 0), (0, 1), (1,0), (0, -1)]:
                ni, nj = k+i, j+l
                if ni>=0 and ni<len(grid) and nj>=0 and nj<len(grid) and grid[ni][nj]==0:
                    grid[ni][nj]=c+1
                    q.append([(ni, nj), c+1])
        return res if res else -1
