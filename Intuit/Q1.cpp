class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        N = len(points)
        dist = defaultdict(lambda: Counter())
        
        for i in range(N):
            for j in range(N):
                if i != j:
                    x = (points[j][0] - points[i][0])**2
                    y = (points[j][1] - points[i][1])**2
                    dist[i][x + y] += 1
        answer = 0
        for i in range(N):
            for k,v in dist[i].items():
                if v > 1:
                    answer += factorial(v) // factorial(v-2)
        return answer
