class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        def bfs(cache):
            queue = collections.deque(list(cache))
            while queue:
                x, y = queue.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row, col = x + dx, y + dy
                    if 0 <= row < rows and 0 <= col < cols and heights[row][col] >= heights[x][y] and (row, col) not in cache:
                        queue.append((row, col))
                        cache.add((row, col))
            return cache

        rows, cols = len(heights), len(heights[0])
        
        upper_left, lower_right = set(), set()
        
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    upper_left.add((row, col))
                if row == rows - 1 or col == cols - 1:
                    lower_right.add((row, col))

        upper_left = bfs(upper_left)
        lower_right = bfs(lower_right)
        
        return list(upper_left.intersection(lower_right))
