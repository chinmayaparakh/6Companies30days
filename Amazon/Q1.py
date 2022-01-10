//TLE using Python therefore also used C++ on the same question
class Solution:
    def maxProfit(self, K, N, A):
        # code here
        profit = [[0 for i in range(K + 1)]for j in range(N)]
        
        for i in range(1, N):
            
            for j in range(1, K + 1):
                mx=0
                
                for l in range(i):
                    mx = max(mx,A[i]-A[l]+profit[l][j-1])
                
                profit[i][j] = max(profit[i - 1][j], mx)
        
        return profit[N-1][K]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends
