class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for length in range(2, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1
                dp[left][right] = float('inf')
                for k in range(left + 1, right):
                    dp[left][right] = min(dp[left][right], max(dp[left][k - 1], dp[k + 1][right]) + k)
                if left + 1 == right:
                    dp[left][left + 1] = left
        return dp[1][n]
