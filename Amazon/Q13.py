class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        c = 0
        q = deque()
        lst = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    lst.append((i,j))
        if lst:
            q.append(lst)
                    
        while q:
            s = q.popleft()
            rot = 0
            t = []
            for (i, j) in s:
                for (k, l) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if (0 <= k <= m - 1) and (0 <= l <= n - 1) and (grid[k][l] == 1):
                        rot = 1
                        grid[k][l] = 2
                        t.append((k, l))
            if rot:
                c += 1
            if t:
                q.append(t)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return c
